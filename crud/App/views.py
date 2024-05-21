from django.shortcuts import render,redirect
from .models import Employee
from .forms import *
# Create your views here.
def home(request):
    return render (request,'App/home.html')

def child(request):
    employee=Employee.objects.all()
    context={'employee':employee}
    return render (request,'App/child.html',context)

def add(request):
    fm = AddEmployee()
    fmadd = AddEmployee(request.POST)
    if fmadd.is_valid():
        fmadd.save()
        return redirect('/')
    context={'form':fm}
    return render(request, 'App/add.html',context)

def delete(request):
    data=request.POST
    id=data.get('id')
    empdata=Employee.objects.get(id=id)
    empdata.delete()
    return redirect('/')

def edit(request,id):
    empdata=Employee.objects.get(id=id)
    fm = AddEmployee(instance=empdata)
    editform=AddEmployee(request.POST,instance=empdata)
    if editform.is_valid():
        editform.save()
        return redirect('/')
    context={'form':fm,}
    return render(request, 'App/edit.html',context)
