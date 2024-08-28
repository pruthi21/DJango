from django.shortcuts import render,redirect
from .models import EmpForm, Emp,Account, AccountForm

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
    