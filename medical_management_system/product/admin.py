from django.contrib import admin

# Register your models here.
from .models import PharmacyProduct,Category

# Register your models here.
admin.site.register(PharmacyProduct)
admin.site.register(Category)