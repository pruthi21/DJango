from django.contrib import admin
from .models import Poster , Category, Product

# Register your models here.
admin.site.register(Poster)
admin.site.register(Category)
admin.site.register(Product)