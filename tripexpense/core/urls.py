from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('show/',views.expense_list,name='expense_list'),
    path('expense/<int:expense_id>/delete/', views.expense_delete, name='expense_delete'),
]