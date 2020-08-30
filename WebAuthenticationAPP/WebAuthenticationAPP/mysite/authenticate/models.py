from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Patient(models.Model):
    first_name=models.CharField(max_length=100)
    second_name=models.CharField(max_length=100)
    Age=models.IntegerField(default=0)
    mobile_phone=models.IntegerField(default=0)
    date_registered=models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.first_name

class Patient_Diagnosis(models.Model):
    Diagnosis=models.CharField(max_length=255)
    diagnosis_detail=models.TextField()
    date_of_diagnosis=models.DateTimeField(default=timezone.now)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    nurse=models.ForeignKey(User,on_delete=models.CASCADE)
    report=models.TextField()




    def __str__(self):
        return self.Diagnosis
