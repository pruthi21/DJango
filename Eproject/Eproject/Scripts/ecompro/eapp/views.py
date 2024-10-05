from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method=='POST':
        f=UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserCreationForm
        context={'form':f}
        return render(request,'register.html',context)

def login_view(request):
    if request.method=='POST':

        uname=request.POST.get('username')
        passw=request.POST.get('password')

        user=authenticate(request,username=uname,password=passw)

        if user is not None:
            request.session['uid']=user.id
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/')

def product_list(request):

    pl=Product.objects.all()
    duplicate_cate=set()
    for i in pl:
        duplicate_cate.add(i.category)
        context={'pl':pl, 'duplicate_cate': duplicate_cate}
        return render(request,'plist.html',context)

def cato_wise_pro(request,id):
    pl=Product.objects.all()
    duplicate_cate=set()
    for i in pl:
        duplicate_cate.add(i.category)
        pl=Product.objects.filter(category=id)
    context={'duplicate_cate':duplicate_cate,'pl':pl}
    return render(request,'plist.html',context)

def add_to_cart(request, pid):
    product_id=Product.objects.get(id=pid)
    user_id= request.session.get('uid')
    user= User.objects.get(id=user_id)
    c= Cart()
    c.products=product_id
    c.user=user
    c.save()
    return redirect('/')

def cart_list(request):
    user_id=request.session.get('uid')
    user= User.objects.get(id=user_id)
    cl= Cart.objects.filter(user=user_id)
    context={'cl':cl}
    return render(request, 'clist.html', context)