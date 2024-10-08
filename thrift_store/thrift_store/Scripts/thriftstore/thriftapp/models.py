from django.db import models

# Create your models here.
class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    description=models.TextField(max_length=300,default='',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name
    class Meta:
        db_table='product'