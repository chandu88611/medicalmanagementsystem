# models.py

from django.db import models
from users.models import CustomUser
from customers.models import Customer
from product.models import PharmacyProduct
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Bill(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    invoice_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    receipt_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    is_invoice = models.BooleanField(default=True)
    is_receipt = models.BooleanField(default=False)
    products = models.ManyToManyField(PharmacyProduct, through='BillProduct')

    def save(self, *args, **kwargs):
        if not self.invoice_number and self.is_invoice:
            last_invoice = Bill.objects.filter(
                is_invoice=True).order_by('-invoice_number').first()
            if last_invoice:
                last_number = int(last_invoice.invoice_number.split('-')[1])
                self.invoice_number = f'INV-{str(last_number + 1).zfill(4)}'
            else:
                self.invoice_number = 'INV-0001'

        if not self.receipt_number and self.is_receipt:
            last_receipt = Bill.objects.filter(
                is_receipt=True).order_by('-receipt_number').first()
            if last_receipt:
                last_number = int(last_receipt.receipt_number.split('-')[1])
                self.receipt_number = f'RECEIPT-{str(last_number + 1).zfill(4)}'
            else:
                self.receipt_number = 'RECEIPT-0001'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.invoice_number if self.is_invoice else self.receipt_number


class BillProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(PharmacyProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return f"{self.product} - {self.quantity}"
