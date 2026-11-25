from django.urls import path
from .views import *
urlpatterns=[
    path('register/', Registerpage, name='register'),
    path('login/',loginpage,name="login"),
    path('logout/',user_logout, name='logout'),
    path('dashboard/',dashboard, name='dashboard'),
    path('add-income/',add_income, name='add_income'),
    path('add-expense/',add_expense, name='add_expense'),
    path('transactions/',transactions, name='transactions'),
    path('edit-income/<int:id>/',edit_income, name='edit_income'),
    path('delete-income/<int:id>/', delete_income, name='delete_income'),
    path('edit-expense/<int:id>/',edit_expense, name='edit_expense'),
    path('delete-expense/<int:id>/',delete_expense, name='delete_expense'),
]