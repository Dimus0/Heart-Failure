from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser
import numpy as np



class CustomUserManager(BaseUserManager):
    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError("You did not entered a valid email address! ")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(email,password,**extra_fields)


class CustomUser(AbstractBaseUser):
    first_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.EmailField(unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email


class PatientIndicator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='indicators')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')], default="")
    height = models.PositiveIntegerField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    is_smoke = models.BooleanField(default=False)
    is_alco = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    gluc = models.FloatField(help_text="Glucose level")
    cholesterol = models.FloatField(help_text="Cholesterol level")
    ap_hi = models.PositiveIntegerField(help_text="Systolic blood pressure")
    ap_lo = models.PositiveIntegerField(help_text="Diastolic blood pressure")
    

    def __str__(self):
        return f'{self.user.name} {self.user.surname} (ID: {self.pk})'

    def calculate_bmi_value(self):
        if self.height > 0:
            height_in_meters = self.height / 100
            return round(self.weight / (height_in_meters ** 2), 2)
        return None

    def calculate_pulse_index_value(self):
        if self.ap_hi > 0:
            pulse_pressure = self.ap_hi - self.ap_lo
            return round(pulse_pressure / self.ap_hi, 2)
        return None
