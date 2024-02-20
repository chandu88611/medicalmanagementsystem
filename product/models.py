from django.db import models
from users.models import CustomUser # Import the User model from Django's auth module

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class PharmacyProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_pack = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Price per pack
    price_per_sheet = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Price per sheet
    expiration_date = models.DateField()
    batch_number = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    barcode = models.CharField(max_length=20)  # New field for barcode
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    # Fields for tablets
    tablets_per_sheet = models.PositiveIntegerField(default=1)
    sheets_per_pack = models.PositiveIntegerField(default=1)
    # Field for other products
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


    # def available_quantity(self):
    #     if self.tablets_per_sheet > 1 or self.tablets_per_pack > 1:
    #         return self.quantity_single_tablet + \
    #                (self.quantity_per_sheet * self.tablets_per_sheet) + \
    #                (self.quantity_per_pack * self.tablets_per_pack)
    #     else:
    #         return self.quantity_other

    # def sell_units(self, quantity, unit_type):
    #     if unit_type == 'single_tablet':
    #         self.quantity_single_tablet -= quantity
    #     elif unit_type == 'per_sheet':
    #         self.quantity_per_sheet -= quantity
    #     elif unit_type == 'per_pack':
    #         self.quantity_per_pack -= quantity
    #     else:
    #         self.quantity_other -= quantity
    #     self.save()
