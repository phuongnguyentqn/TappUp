"""
Model User
"""
from django.conf import settings
from django.db import models

from tapp_up.models.base import BaseModel


class Expense(BaseModel):
    """
    Define all attributes and methods of Expense
    """
    consumer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    quantity = models.IntegerField()
    expense_date = models.DateTimeField()
    good_type = models.CharField(max_length=126)

    def __str__(self):
        return f'{self.quantity} VND by User[{self.consumer}]' \
            ' on {self.good_type} at {self.expense_date}'
