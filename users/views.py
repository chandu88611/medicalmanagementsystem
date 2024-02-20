# user/views.py
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, CustomUserLoginSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def custom_user_signup(request):
    if request.method == 'POST':
        print(request.data)
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# class CustomUserLoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([AllowAny])
def custom_user_login(request):
    serializer = CustomUserLoginSerializer(data=request.data)
    if serializer.is_valid():
        user = authenticate(request, email=serializer.validated_data['email'], password=serializer.validated_data['password'])
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            response={
                'status':True,
                'access_token':access_token,
                'refresh_token':refresh_token,
                'data':CustomUserSerializer(user).data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_protected_data(request):
    user_data = {
        'email': request.user.email,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'roles': request.user.roles,
        # Add any other fields you want to include in the response
    }
    return Response(user_data, status=status.HTTP_200_OK)    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users_with_roles(request):
    # Check if the requesting user has the 'admin' role
    if request.user.roles != 'admin':
        return Response({'detail': 'You do not have permission to access this resource.'}, status=status.HTTP_403_FORBIDDEN)

    # Retrieve all users with their role user
    users = CustomUser.objects.filter(roles='user')
    serializer = CustomUserSerializer(users, many=True)
    response={
        "status":True,
        "message":'Users Fetched Succesfully',
        "data":serializer.data
    }
    return Response(response, status=status.HTTP_200_OK)    



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def custom_user_logout(request):
    # Get the refresh token from the request
    # refresh_token = request.data.get('refresh_token')
    refresh_token = request.headers.get('Authorization').split(' ')[1]

    if not refresh_token:
        return Response({'detail': 'Refresh token is required for logout.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Blacklist the refresh token to invalidate it
        RefreshToken(refresh_token).blacklist()

        return Response({"status":True,'detail': 'Logout successful.'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': f'Error during logout: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)