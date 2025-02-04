from datetime import datetime 
from django.http import HttpResponse
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
def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept_id = int(request.POST['dept'])
        role_id = int(request.POST['role'])
        new_emp = Employe(
            first_name=first_name,
            last_name=last_name,
            salary=salary,
            bonous=bonus,
            Phone=phone,
            dept_id=dept_id,
            Role_id=role_id,
            hire_date=datetime.now()
        )
        new_emp.save()
        return HttpResponse("Employee added Successfully")
    elif request.method == 'GET':
        departments = dept.objects.all()  # Fetch all departments
        roles = Role.objects.all()  # Fetch all roles
        context = {
            'departments': departments,
            'roles': roles
        }
        return render(request, 'add_emp.html', context)
    else:
        return HttpResponse("An error occurred")