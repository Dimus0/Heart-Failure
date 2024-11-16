from django.db import models
from django.conf import settings

class PatientIndicator(models.Model):
    user = models.ForeignKey( 
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_indicators'
    )
    name = models.CharField(max_length=20, default="")
    surname = models.CharField(max_length=50, default="")
    age = models.PositiveIntegerField() 
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default="")
    bmi = models.FloatField() 
    is_smoke = models.BooleanField(default=False)
    is_alco = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    gluc = models.PositiveSmallIntegerField() 
    cholesterol = models.PositiveSmallIntegerField()
    ap_hi = models.IntegerField()
    ap_lo = models.IntegerField()

    def __str__(self):
        return f'{self.name} {self.surname} (ID: {self.pk})'

