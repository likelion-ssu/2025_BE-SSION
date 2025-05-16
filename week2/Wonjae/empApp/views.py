from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeeData(request):
    employees = Employee.objects.all() #sql언어로 select * from empapp_employee; 랑 같음
    empDict = {'employees':employees}
    return render(request,'employees.html', empDict)