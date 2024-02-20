# urls.py
from django.urls import path
from .views import get_all_customers, add_customer, edit_customer, delete_customer

urlpatterns = [
    path('customers/', get_all_customers, name='get_all_customers'),
    path('customers/add/', add_customer, name='add_customer'),
    path('customers/edit/<int:pk>/', edit_customer, name='edit_customer'),
    path('customers/delete/<int:pk>/', delete_customer, name='delete_customer'),
]
