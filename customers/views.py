from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer  # You need to create a serializer for the Customer model

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_customers(request):
    try:
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'status': 'success', 'message': 'Customers retrieved successfully', 'data': serializer.data})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_customer(request):
    try:
        data = request.data.copy()
        data['user'] = request.user.id
        existing_customer = Customer.objects.filter(phone_number=data['phone_number']).first()
        if existing_customer:
            return Response({'status': 'error', 'message': 'Customer with the same phone number already exists', 'data': None}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Customer added successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'error', 'message': serializer.errors, 'data': None}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'Customer updated successfully', 'data': serializer.data})
        else:
            return Response({'status': 'error', 'message': serializer.errors, 'data': None}, status=status.HTTP_400_BAD_REQUEST)
    except Customer.DoesNotExist:
        return Response({'status': 'error', 'message': 'Customer not found', 'data': None}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response({'status': 'success', 'message': 'Customer deleted successfully', 'data': None})
    except Customer.DoesNotExist:
        return Response({'status': 'error', 'message': 'Customer not found', 'data': None}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e), 'data': None}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
