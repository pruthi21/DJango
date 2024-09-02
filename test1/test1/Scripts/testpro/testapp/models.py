from django.db import models
from django import forms

# Create your models here.
class Student(models.Model):
    Name= models.CharField(max_length=30)
    Age= models.IntegerField()
    Rollno= models.CharField(max_length=30)
    Class= models.CharField(max_length=30)
    Contact= models.CharField(max_length=30)
    Address= models.CharField(max_length=30)

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.Name

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'
      


