from django.shortcuts import render
from .models import Employe,Role,dept
# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps=Employe.objects.all()
    context={
        "emps":emps
    }
    return render(request,'view_all.html',context)