from django.shortcuts import render
from empApp.models import Employee
# Create your views here.

def employeeData(request):
    employee = Employee.objects.all()
    empDict = {'employee' : employee}
    return render(request, 'employee.html', context=empDict)
