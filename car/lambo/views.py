from django.shortcuts import render

# Create your views here.
def lambo(request):
    return render (request,'lambo/lambo.html')