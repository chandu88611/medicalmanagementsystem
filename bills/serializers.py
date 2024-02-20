# serializers.py

from rest_framework import serializers
from .models import Bill, BillProduct
from users.models import CustomUser

class BillProductSerializer(serializers.ModelSerializer):

    quantity = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    class Meta:
        model = BillProduct
        fields = [  'quantity', 'amount']

    def get_quantity(self, obj):
        products_data = self.context['request'].data.get('products', [])
        for product_data in products_data:
            print( product_data,obj.id)
            if product_data.get('product') == obj.id:
                return product_data.get('quantity')
        return None

    def get_amount(self, obj):
        products_data = self.context['request'].data.get('products', [])
        for product_data in products_data:
            if product_data.get('product') == obj.id:
                return product_data.get('amount')
        return None


class BillSerializer(serializers.ModelSerializer):
    products = BillProductSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ['id', 'user', 'customer', 'date', 'amount', 'description', 'invoice_number', 'receipt_number', 'is_invoice', 'is_receipt', 'products']
