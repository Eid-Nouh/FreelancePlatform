from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user_type = models.CharField(
        max_length=10,
        choices=[('freelancer', 'مستقل')],  # فقط مستقل
        default='freelancer'
    )
    
    def __str__(self):
        return self.username