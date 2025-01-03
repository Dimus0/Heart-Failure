from django.contrib import admin
from django.urls import path, re_path,include
# from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import PatientIndicatorsView,GetRecommendationsView
from django.views.generic import TemplateView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Heart Risk Prediction API",
      default_version='v1',
      description="API для передбачення ризику серцевих захворювань",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@myapi.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('api/heart-risk/predict', GetRecommendationsView.as_view(), name='heart-risk-predict'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]
