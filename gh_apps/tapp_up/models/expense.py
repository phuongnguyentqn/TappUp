"""
Model User
"""
from django.conf import settings
from django.db import models

from tapp_up.models.base import BaseModel


class Category(BaseModel):
    """
    Expense category
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        """
        Object as string
        """
        return f'{self.name}'


class Expense(BaseModel):
    """
    Define all attributes and methods of Expense
    """
    consumer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    expense_date = models.DateTimeField()
    good_type = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.quantity} VND by User[{self.consumer}]' \
            f' on {self.good_type} at {self.expense_date}'
