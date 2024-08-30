from django.shortcuts import render
from django.views.generic import FormView,CreateView
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