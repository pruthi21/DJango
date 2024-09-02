from django.shortcuts import render
from django.views.generic import FormView,CreateView,DeleteView,ListView,UpdateView
from .models import StudentForm

# Create your views here.
def home(request):
    return render(request,'home.html')

class add_student(FormView):
    form_class= StudentForm
    template_name='addstudent.html'
