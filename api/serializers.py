from  rest_framework import serializers
from django.contrib.auth.models import User
from .models import PatientIndicator

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model= User
        fields = ['id','username','password','email']


class PatientIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientIndicator
        fields = ('name','surname','age','gender','height','weight','is_smoke','is_alco',
                  'is_active','gluc','cholesterol','ap_hi','ap_lo')