from django.shortcuts import render
from studentApp.models import Student
# Create your views here.

def studentData(request):
    student = Student.objects.all()
    studentDict = {'student' : student}
    return render(request, 'student.html', context=studentDict)
