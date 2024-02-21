from django.urls import path
from .views import (
    category_list_create,
    category_detail,
    pharmacy_product_list_create,
    pharmacy_product_detail,
    total_stock_value
)

urlpatterns = [
    path('categories/', category_list_create, name='category-list-create'),
    path('categories/<int:pk>/', category_detail, name='category-detail'),

    path('pharmacy_products/', pharmacy_product_list_create, name='pharmacy-product-list-create'),
    path('pharmacy_products/<int:pk>/', pharmacy_product_detail, name='pharmacy-product-detail'),
    path('total_stock_value/', total_stock_value, name='total_stock_value'),
]
