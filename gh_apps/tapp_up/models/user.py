"""
Model User
"""
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Grasshopper(AbstractUser):
    """
    Define all attributes and methods of Grasshopper
    """
    email = models.EmailField(_('email address'), blank=True, unique=True)
    is_owner = models.BooleanField(default=False)

    class Meta:
        db_table = 'gh_user'

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.email

    def __str__(self):
        return self.full_name
