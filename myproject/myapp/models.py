from django.db import models

# Create your models here.
class Feature(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=500)
    is_true=models.BooleanField(default=True)#database migrated to myapp.0001

# class Services(models.Model):
#     name=models.CharField(max_length=100)
#     details=models.CharField(max_length=500)
#     color=models.CharField(max_length=30)
