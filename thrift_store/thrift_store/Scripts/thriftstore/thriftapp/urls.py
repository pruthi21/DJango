"""
URL configuration for thriftstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_v
from . import views as v 
from .views import products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home, name= 'home'),
    path('products',v.products, name= 'products'),
    path('<int:id>',v.add, name='add'),
    path('about', v.about, name= 'about'),
    path('contact', v.contact, name='contact'),
    path('cart', v.cart, name='cart'),
    path('account', v.account, name='account'),
    path('signup', v.signup, name='signup'),
    path('login', auth_v.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_v.LogoutView.as_view(), name='logout'),
    
    
]
