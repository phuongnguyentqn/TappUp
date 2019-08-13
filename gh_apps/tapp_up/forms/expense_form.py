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
    
    def __init__(self, *args, **kwargs):
        """
        Override constructor to add class to field
        """
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            default_cls = visible.field.widget.attrs.get('class')
            print(default_cls)
            if default_cls != 'datepicker':
                visible.field.widget.attrs['class'] = 'form-control'
            else:
                visible.field.widget.attrs['class'] = 'form-control date datepicker'
