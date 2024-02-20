from django.db import models
from users.models import  CustomUser # Import the User model from Django's auth module
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Customer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)  # User field to associate customers with specific users
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, validators=[MinLengthValidator(10), MaxLengthValidator(10)])
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
