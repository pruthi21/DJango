from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Product(models.Model):
    name= models.CharField(max_length=30)
    price= models.IntegerField(default=0)
    discreption= models.TextField(max_length=300,default='',null=True,blank=True)
    name= models.ForeignKey(Category , on_delete= models.CASCADE)
    image=models.ImageField(upload_to='image')
