from django import forms

from ..models import Expense


class ExpenseForm(forms.ModelForm):
    """
    Custom form for handle Expense input data
    """
    class Meta:
        model = Expense
        fields = ['consumer', 'quantity', 'expense_date', 'good_type']
        widgets = {
            'expense_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
