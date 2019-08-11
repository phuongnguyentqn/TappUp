from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from tapp_up.models import Expense
from tapp_up.forms import ExpenseForm


class GhLoginRequiredMixin(LoginRequiredMixin):
    """
    CBV mixin that gives access mixins the same customizable
    functionality.
    """
    login_url = '/login/'


class HomeView(TemplateView):
    """
    Home page view
    """
    template_name = 'pages/home.html'


class LoginView(TemplateView):
    """
    Login page view
    """
    template_name = 'pages/login.html'


class ExpenseList(GhLoginRequiredMixin, ListView):
    """
    List expense of all grasshoppers in a particular period
    """
    model = Expense
    template_name = 'pages/expense_list.html'


class AddExpennseView(GhLoginRequiredMixin, CreateView):
    """
    Add new expense view
    Refer: https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/
    """
    template_name = 'forms/expense_form.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('tapp_up:expense-list')
