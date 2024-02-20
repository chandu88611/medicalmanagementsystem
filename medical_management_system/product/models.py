from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PharmacyProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField()
    batch_number = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)  # New field for barcode
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
