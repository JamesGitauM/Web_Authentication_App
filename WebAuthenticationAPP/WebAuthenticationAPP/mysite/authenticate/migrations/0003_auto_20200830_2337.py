# Generated by Django 3.1 on 2020-08-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_patient_patient_diagnosis'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='Age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='mobile_phone',
            field=models.IntegerField(default=0),
        ),
    ]
