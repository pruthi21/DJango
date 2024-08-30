from django.db import models
from django import forms

# Create your models here.
class Emp(models.Model):
    name= models.CharField(max_length=30)
    age= models.IntegerField()
    email= models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    contact= models.CharField(max_length=30)

    class Meta:
        db_table='emp'

class EmpForm(forms.ModelForm):
    class Meta:
        model= Emp
        fields='__all__'
      
        



