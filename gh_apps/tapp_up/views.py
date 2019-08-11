from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from tapp_up.forms import ExpenseForm


class GhLoginRequiredMixin(LoginRequiredMixin):
    """
    CBV mixin that gives access mixins the same customizable
    functionality.
    """
    login_url = 'login/'


class HomeView(TemplateView):
    """
    Home page view
    """
    template_name = "pages/home.html"


class AddExpennseView(GhLoginRequiredMixin, CreateView):
    """
    Add new expense view
    Refer: https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/
    """
    template_name = 'forms/expense_form.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('tapp_up:expense-add')
