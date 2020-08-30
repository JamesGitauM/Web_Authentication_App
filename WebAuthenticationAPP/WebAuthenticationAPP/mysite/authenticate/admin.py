from django.contrib import admin
from authenticate import models

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Patient_Diagnosis)
admin.site.register(models.Patient)
