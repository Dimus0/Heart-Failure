from django.db import models
from django.conf import settings
import numpy as np

class PatientIndicator(models.Model):
    user = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    name = models.CharField(max_length=20, default="")
    surname = models.CharField(max_length=50, default="")
    age = models.PositiveIntegerField() 
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default="")
    height = models.IntegerField()
    weight = models.FloatField()
    is_smoke = models.BooleanField(default=False)
    is_alco = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    gluc = models.FloatField() 
    cholesterol = models.FloatField()
    ap_hi = models.IntegerField()
    ap_lo = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname} (ID: {self.pk})'
    
    def calculate_bmi_value(self):
        return self.weight / (np.sqrt(self.height)) 
    
    def calculate_pulse_index_value(self):
        pulse_pressure = self.ap_hi - self.ap_lo
        return pulse_pressure / self.ap_hi

