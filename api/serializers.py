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
        fields = ('age','gender','height','weight','is_smoke','is_alco',
                  'is_active','gluc','cholesterol','ap_hi','ap_lo')
        
class PatientIndicatorsSerializers(serializers.Serializer):
    age = serializers.IntegerField(min_value=0, max_value=120)
    gender = serializers.ChoiceField(choices=[(0, 'Female'), (1, 'Male')])
    height = serializers.FloatField(min_value=50, max_value=250)
    weight = serializers.FloatField(min_value=20, max_value=300)
    is_smoke = serializers.BooleanField()
    is_alco = serializers.BooleanField()
    is_active = serializers.BooleanField()
    gluc = serializers.ChoiceField(choices=[(1, 'Normal'), (2, 'Above Normal'), (3, 'Well Above Normal')])
    cholesterol = serializers.ChoiceField(choices=[(1, 'Normal'), (2, 'Above Normal'), (3, 'Well Above Normal')])
    ap_hi = serializers.IntegerField(min_value=50, max_value=300)
    ap_lo = serializers.IntegerField(min_value=30, max_value=200)