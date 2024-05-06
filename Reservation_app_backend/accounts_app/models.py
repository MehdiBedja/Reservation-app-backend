# accounts_app/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_image = models.CharField(max_length=255, blank=True, null=True)
    # Add other custom fields as needed

    def __str__(self):
        return self.username
