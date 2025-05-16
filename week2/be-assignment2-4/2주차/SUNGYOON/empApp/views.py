from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeeData(request):
    employees = Employee.objects.all() #오브젝트 올은 모든 속성들을 가져오겠다
    empDict = {'employees': employees}  
    return render(request, 'employees.html', empDict)