from rest_framework import serializers
from .models import Category, PharmacyProduct

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PharmacyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyProduct
        fields = '__all__'
