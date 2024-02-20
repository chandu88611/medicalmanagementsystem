# urls.py

from django.urls import path
from .views import generate_bill

urlpatterns = [
    path('generate-bill/', generate_bill, name='generate_bill'),
    # Other URLs for your app
]
