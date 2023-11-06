from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_STATUS_CHOICES = (
        ('owner', 'Owner'),
        ('superuser', 'Superuser'),
        ('staff', 'Staff'),
    )
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    user_status = models.CharField(max_length=10, choices=USER_STATUS_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username
