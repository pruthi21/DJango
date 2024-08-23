from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    age=models.IntegerField()

    class  Meta:
        db_table = 'emp'

from django import forms
class EmpForm(forms.ModelForm):
    class Meta:
        model=emp
        fields='__all__'
        