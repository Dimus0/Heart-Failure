# Generated by Django 5.1.1 on 2024-11-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_bmi_patientindicator_weight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientindicator',
            name='cholesterol',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='patientindicator',
            name='gluc',
            field=models.FloatField(),
        ),
    ]
