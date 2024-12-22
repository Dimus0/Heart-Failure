from django.contrib import admin
from django.urls import path, re_path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import PatientIndicatorsView,get_recommendations,GetRecommendationsView
from django.views.generic import TemplateView

urlpatterns = [
    path('model_predict/', get_recommendations),
    path('model/',GetRecommendationsView.as_view(), name='model'),
    path('api/heart-risk/predict', GetRecommendationsView.as_view(), name='heart-risk-predict'),
]
