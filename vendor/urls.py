from django.urls import path, include
from . import views

app_name = 'vendor'


urlpatterns = [
    path('', views.profile, name='Profile'),
    path('accounts/', views.accounts, name='accounts'),
    path('inventory/', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('order/', views.order, name='order'),
]
