"""
Model User
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class Grasshopper(AbstractUser):
    """
    Define all attributes and methods of Grasshopper
    """
    is_owner = models.BooleanField(default=False)

    class Meta:
        db_table = 'gh_user'

    def __str__(self):
        return f'User[{self.email}]'
