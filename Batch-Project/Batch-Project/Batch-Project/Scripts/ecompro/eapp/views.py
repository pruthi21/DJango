from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import Product,Category,Cart
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_user(request):
    if request.method=='POST':
        f = UserCreationForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f = UserCreationForm()
        context ={'form':f}
        return render(request,'register.html',context)
    
def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password') 

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
    context={'pl':pl, 'duplicate_cate':duplicate_cate}
    return render(request,'plist.html',context)

def cato_wise_pro(request,id):
    pl=Product.objects.all()
    duplicate_cate=set()
    for i in pl:
        duplicate_cate.add(i.category)
        pl=Product.objects.filter(category=id)
    context={'duplicate_cate':duplicate_cate,'pl':pl}
    return render(request,'plist.html',context)


def add_to_cart(request,pid):
    product_id = Product.objects.get(id=pid)
    user_id =request.session.get('uid')
    user = User.objects.get(id=user_id)
    cart_item, created = Cart.objects.get_or_create(product=product_id, user=user)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.quantity = 1
        cart_item.save()
    return redirect('/plist')


def cart_list(request):
    user_id = request.session.get('uid')
    print(user_id)
    cart_items = Cart.objects.filter(user_id=user_id)
    print(cart_items)

    cart_with_subtotals = [
        {
            'item':item,
            'subtotal': item.product.price * item.quantity
        }for item in cart_items
    ]
    total_price = sum(item['subtotal'] for item in cart_with_subtotals)

    context={
        'cl': cart_with_subtotals,
        'total_price': total_price
    }
    return render(request,'clist.html',context)

def delete_cart_item(request, cart_id):
    print(cart_id)
    user_id = request.session.get('uid')
    cart_item = Cart.objects.get(id=cart_id, user_id=user_id)
    cart_item.delete()
    return redirect('/clist') 

def product_search(request):
    srch = request.POST.get('srch')
    if srch:
        pl = Product.objects.filter(name__icontains=srch)| Product.objects.filter(description__icontains=srch)
    else:
        pl= Product.objects.none()

    context ={'pl': pl}
    return render(request, 'plist.html', context)