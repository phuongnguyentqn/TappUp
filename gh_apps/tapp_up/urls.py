from django.urls import path

from .views import AddExpennseView, HomeView


app_name = 'tapp_up'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('expense/add/', AddExpennseView.as_view(), name='expense-add'),
]
