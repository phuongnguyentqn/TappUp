from django.urls import path

from . import views


app_name = 'tapp_up'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('expenses/', views.ExpenseList.as_view(), name='expense-list'),
    path('expense/add/', views.AddExpennseView.as_view(), name='expense-add'),
]
