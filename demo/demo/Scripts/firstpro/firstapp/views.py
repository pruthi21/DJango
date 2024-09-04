from django.shortcuts import render,redirect
from .models import EmpForm, Emp,Account, AccountForm
from django.contrib import messages as m 

# Create your views here.
def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=='POST':
        f=EmpForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=EmpForm
        context={'form':f}
        return render(request,'addemp.html',context)

def emp_list(request):
    el=Emp.objects.all()
    context={'el':el}
    return render(request,'emp_list.html',context)

def add_account(request):
    if request.method=='POST':
        f=AccountForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=AccountForm
        context={'form':f}
        return render(request,'account.html',context)

def acc_list(request):
    al = Account.objects.all()
    context={'al':al}
    return render(request,'acclist.html',context)

def delete_emp(request):
    eid=request.GET.get('id')
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/elist')

def delete2_emp(request,eid):#secondmethodof_delete
    
    emp=Emp.objects.get(id=eid)
    emp.delete()
    return redirect('/elist')

def edit_emp(request,eid):
    a = Emp.objects.get(id=eid)
    if request.method=='POST':
        f=EmpForm(request.POST,instance=a)
        f.save()
        return redirect('/')
    else:
        f=EmpForm(instance=a)
        context={'form':f}
        return render(request,'addemp.html',context)

def msg1_data(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        if(uname=='pruthikaw' and passw=='pruthikaw21'):
            lmsg="LOGIN SUCESSFULLY"
            smsg='Username is: '+uname+' '+'password is: '+passw
            context={'lmsg':lmsg,'smsg':smsg}
            return render(request,'msg.html',context)
        else:
            emsg='LOGIN ERROR'
            smsg='Username is :'+uname+' '+'password is: '+passw
            context={'emsg':emsg,'smsg':smsg}
            return render(request,'msg.html',context)

    else:
        context={'fmsg':'This is first msg by using render'}
        return render(request,'msg.html',context)
    
def msg2_data(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')
        if(uname=='yash'and passw=='Yash@1925'):
            m.success(request,'Login Successfully')
            m.info(request, 'Username is: '+uname+' and Password is: '+passw)
            return render(request,'msg2.html')
        else:
            m.error(request,'Login Failed')
            m.info(request, 'Username is: '+uname+' and Password is: '+passw)
            m.warning(request,'Please Enter Valid Username and Password')
            return render(request,'msg2.html')
    else:
        m.add_message(request,m.INFO,'This is django messages app')
        m.add_message(request,m.INFO,'Login Form')
        m.warning(request,'Please Enter Valid Username and Password')
        return render(request,'msg2.html')