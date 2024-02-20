from django.db import models
from django.contrib.auth.models import User  # Import the User model from Django's auth module

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User field to associate customers with specific users
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
