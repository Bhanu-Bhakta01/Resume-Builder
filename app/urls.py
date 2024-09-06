from django.urls import path
from .views import personal_info_view
from django.shortcuts import render, redirect

urlpatterns = [
    path('', personal_info_view, name='personal_info_form'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),  # Optional success page
]
