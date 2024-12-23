from django.contrib import admin
from django.urls import path, re_path,include
# from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import PatientIndicatorsView,GetRecommendationsView
from django.views.generic import TemplateView

urlpatterns = [
    path('api/heart-risk/predict', GetRecommendationsView.as_view(), name='heart-risk-predict'),
]
