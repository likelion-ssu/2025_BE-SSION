from django.shortcuts import render
from studentApp.models import student

# Create your views here.
def studentData(request):
    students = student.objects.all() #오브젝트 올은 모든 속성들을 가져오겠다
    stuDict = {'students': students}  
    return render(request, 'students.html', stuDict)
# Create your views here.
