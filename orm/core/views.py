from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    hero = Student.objects.all()
    return render(request, 'core/index.html',{'hero': hero})