from django.shortcuts import render
from studentApp.models import Student

# Create your views here.
def studentData(request):
    students = Student.objects.all()
    studentDict = {'students': students}
    return render(request, 'students.html', studentDict)