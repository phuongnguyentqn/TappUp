""" Expense form """
import datetime

from django import forms
from django.core.exceptions import ValidationError

from ..models import Expense


class ExpenseForm(forms.ModelForm):
    """
    Custom form for handle Expense input data
    """
    class Meta:
        model = Expense
        fields = ['consumer', 'quantity', 'expense_date', 'category']
        

    def __init__(self, *args, **kwargs):
        """
        Override constructor to add class to field
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
