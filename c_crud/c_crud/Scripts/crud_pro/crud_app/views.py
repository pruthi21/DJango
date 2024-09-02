from django.shortcuts import render
from django.views.generic import FormView,CreateView,DeleteView,ListView,UpdateView
from .models import EmpForm,Emp
# Create your views here.
def home(request):
    return render(request,'home.html')

class add_emp(FormView):
    form_class=EmpForm
    template_name='addemp.html'

class create_view(CreateView):
    model=Emp
    fields='__all__'
    success_url="/"

class emp_list(ListView):
    model=Emp
    template_name='emplist.html'

class delete1_view(DeleteView):
     template_name='delete1.html'
     model=Emp
     fields = '__all__'
     success_url='/elist'


class delete2_view(DeleteView):
     model=Emp
     success_url='/elist'


class edit_view(UpdateView):
     model=Emp
     fields='__all__'
     template_name='edit.html'
     success_url='/elist'