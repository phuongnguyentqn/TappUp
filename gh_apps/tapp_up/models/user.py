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
        return self.get_full_name() or self.email

    def __str__(self):
        return f'User[{self.email}]'
