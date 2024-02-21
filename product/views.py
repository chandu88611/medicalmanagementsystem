from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Category, PharmacyProduct
from .serializers import CategorySerializer, PharmacyProductSerializer
from users.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken



@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def category_list_create(request):
    try:
        if request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response({
                "status": True,
                "message": "Category created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        elif request.method == 'GET':
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response({
                "status": True,
                "message": "Categories retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": False,
            "message": f"Error: {str(e)}",
            "data": {}
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def category_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)

        if request.method == 'GET':
            serializer = CategorySerializer(category)
            return Response({
                "status": True,
                "message": "Category retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = CategorySerializer(category, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "status": True,
                "message": "Category updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            category.delete()
            return Response({
                "status": True,
                "message": "Category deleted successfully",
                "data": {}
            }, status=status.HTTP_204_NO_CONTENT)

    except Category.DoesNotExist:
        return Response({
            "status": False,
            "message": "Category not found",
            "data": {}
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "status": False,
            "message": f"Error: {str(e)}",
            "data": {}
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def pharmacy_product_list_create(request):
    try:
        if request.method == 'POST':
            serializer = PharmacyProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            return Response({
                "status": True,
                "message": "Pharmacy product created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        elif request.method == 'GET':
            products = PharmacyProduct.objects.all()
            serializer = PharmacyProductSerializer(products, many=True)
            return Response({
                "status": True,
                "message": "Pharmacy products retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": False,
            "message": f"Error: {str(e)}",
            "data": {}
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def pharmacy_product_detail(request, pk):
    try:
        product = PharmacyProduct.objects.get(pk=pk)

        if request.method == 'GET':
            serializer = PharmacyProductSerializer(product)
            return Response({
                "status": True,
                "message": "Pharmacy product retrieved successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serializer = PharmacyProductSerializer(product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                "status": True,
                "message": "Pharmacy product updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            product.delete()
            return Response({
                "status": True,
                "message": "Pharmacy product deleted successfully",
                "data": {}
            }, status=status.HTTP_204_NO_CONTENT)

    except PharmacyProduct.DoesNotExist:
        return Response({
            "status": False,
            "message": "Pharmacy product not found",
            "data": {}
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "status": False,
            "message": f"Error: {str(e)}",
            "data": {}
        }, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def total_stock_value(request):
    try:
        # Get all pharmacy products
        products = PharmacyProduct.objects.all()
        
        # Calculate total stock value
        total_value = sum(product.price * product.quantity for product in products)
        
        return Response({
            'total_stock_value': total_value
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       