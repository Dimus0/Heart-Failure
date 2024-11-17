# Generated by Django 5.1.1 on 2024-11-16 18:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patientindicator',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='bmi',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='cholesterol',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='gluc',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='is_alco',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='is_smoke',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='surname',
            field=models.CharField(default='', max_length=50),
        ),
    ]
