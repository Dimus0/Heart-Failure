from django.contrib import admin
from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import PatientIndicatorsView

urlpatterns = [
    path('home',PatientIndicatorsView.as_view()),
    
]
