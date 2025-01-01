import random
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import numpy as np
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt
import joblib
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from .models import PatientIndicator
from .serializers import PatientIndicatorsSerializers,PatientIndicatorsSerializer

class PatientIndicatorsView(generics.CreateAPIView):
    queryset = PatientIndicator.objects.all()
    serializer_class = PatientIndicatorsSerializer


model_path = "./api/Gradient_Boosting_model_predict.pkl"
model = joblib.load(model_path)


class GetRecommendationsView(APIView):

    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]

    # def get(self, request, *args, **kwargs):
    #     # Повертає JSON-приклад для тестування
    #     example_data = {
    #         "age": 45,
    #         "gender": 1,
    #         "height": 175,
    #         "weight": 70,
    #         "is_smoke": 0,
    #         "is_alco": 0,
    #         "is_active": 1,
    #         "gluc": 1,
    #         "cholesterol": 2,
    #         "ap_hi": 120,
    #         "ap_lo": 80
    #     }
    #     return JsonResponse({
    #         "message": "Використовуйте POST запит із цими даними:",
    #         "example": example_data
    #     }, status=200)
    
    def post(self, request, *args, **kwargs):
        serializer = PatientIndicatorsSerializers(data=request.data)
        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                
                if validated_data["cholesterol"] == 1:
                    validated_data["cholesterol"] = round(random.uniform(1.0, 5.17), 2)
                elif validated_data["cholesterol"] == 2:
                    validated_data["cholesterol"] = round(random.uniform(5.17, 6.18), 2)
                elif validated_data["cholesterol"] == 3:
                    validated_data["cholesterol"] = round(random.uniform(6.21, 7.21), 2)
                
                if validated_data["gluc"] == 1:
                    validated_data["gluc"] = round(random.uniform(3.5, 5.7), 2)
                elif validated_data["gluc"] == 2:
                    validated_data["gluc"] = round(random.uniform(5.7, 6.9), 2)
                elif validated_data["gluc"] == 3:
                    validated_data["gluc"] = round(random.uniform(7.0, 10.4), 2)

                height_m = validated_data["height"] / 100
                bmi = validated_data["weight"] / (height_m ** 2)

                pulse = validated_data["ap_hi"] - validated_data["ap_lo"]
                pulse_pressure_index = pulse / validated_data["ap_hi"]
                input_data = [
                    validated_data["age"],
                    validated_data["gender"],
                    validated_data["ap_hi"],
                    validated_data["ap_lo"],
                    validated_data["gluc"],
                    validated_data["cholesterol"],
                    validated_data["is_smoke"],
                    validated_data["is_alco"],
                    validated_data["is_active"],
                    bmi,
                    pulse_pressure_index
                ]
                    
                input_array = np.array(input_data).reshape(1, -1)

                prediction_probabilities = model.predict_proba(input_array)
                prediction = prediction_probabilities[0][1]
                print(prediction)

                recommendations = []
                if prediction >= 0.8:
                    recommendations.append("Рекомендацiя: Робіть більше фізичної активності.")
                    recommendations.append("Рекомендацiя: Контролюйте рівень стресу.")
                    recommendations.append("Рекомендацiя: Регулярно відвідуйте лікаря.")
                    disease_probability = prediction
                else:
                    recommendations.append("Рекомендація: У вас все добре))")
                    disease_probability = 1 - prediction 

                return Response({
                    "prediction": int(prediction >= 0.9),  
                    "disease_probability": round(disease_probability * 100,2), 
                    "recommendations": recommendations
                }, status=status.HTTP_200_OK, content_type="application/json; charset=utf-8")

            except Exception as e:
                return Response({"error": f"Помилка: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)