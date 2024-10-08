from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout,authenticate 
from .models import Poster , Product


# Create your views here.
def home(request):
    posters = Poster.objects.all()
    return render(request, 'home.html', {'posters': posters})

def products(request):
    pl=Product.objects.all()
    duplicate_cate=set()
    for i in pl:
        duplicate_cate.add(i.category)
    context={'pl':pl, 'duplicate_cate':duplicate_cate}
    return render(request, 'products.html', context)
                  
def add(request,id):
    pl=Product.objects.all()
    duplicate_cate=set()
    for i in pl:
        duplicate_cate.add(i.category)
        pl=Product.objects.filter(category=id)
    context={'duplicate_cate':duplicate_cate,'pl':pl}
    return render(request,'products.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signup
            return redirect('home')  # Redirect to the homepage after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})