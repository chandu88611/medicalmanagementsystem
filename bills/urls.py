# urls.py

from django.urls import path
from .views import generate_bill,get_all_bills,total_collections

urlpatterns = [
    path('generate-bill/', generate_bill, name='generate_bill'),
    path('get-all-bills/', get_all_bills, name='get_bill'),
    path('total_collections/', total_collections, name='get_bill'),
    # Other URLs for your app
]
