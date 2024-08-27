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

class Account(models.Model):
    salary=models.IntegerField()
    month=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    description=models.TextField(max_length=30)
    emp=models.ForeignKey(emp,on_delete=models.CASCADE)

    class Meta:
        db_table = 'account'

class AccountForm(forms.ModelForm):
     class meta:
        model=Account
        fields='__all__'   
        