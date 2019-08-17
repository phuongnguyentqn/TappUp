""" TappUp views"""
import json

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView

from tapp_up.models import Expense, Grasshopper, Category
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

    def get_context_data(self, **kwargs):
        """
        Add more necessary data to view
        """
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        print(context)
        # Add list of all the user
        grasshopper_qs = Grasshopper.objects.filter(
            email__endswith='grasshopperasia.com'
        ).all()
        consumers = [
            {'id': ghp.id, 'full_name': ghp.full_name}
            for ghp in grasshopper_qs
        ]
        context['consumers'] = json.dumps(consumers)
        # Add list of all categories
        categories = list(Category.objects.values('id', 'name').all())
        context['categories'] = json.dumps(categories)
        # Add current user
        context['current_user'] = self.request.user
        return context


class AddExpennseView(GhLoginRequiredMixin, CreateView):
    """
    Add new expense view
    Refer: https://docs.djangoproject.com/en/2.2/topics/class-based-views/generic-editing/
    """
    template_name = 'forms/expense_form.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('tapp_up:expense-list')

    def form_valid(self, form):
        """If request is ajax, return json data."""
        response = super(AddExpennseView, self).form_valid(form)
        if self.request.is_ajax():
            data = form.cleaned_data
            consumer = data['consumer']
            data['consumer'] = {
                'id': consumer.id,
                'full_name': consumer.full_name,
            }
            category = data['category']
            data['category'] = {
                'id': category.id,
                'name': category.name,
            }
            return JsonResponse(data)
        return response

    def form_invalid(self, form):
        """If request is ajax, return json data."""
        response = super(AddExpennseView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        return response
