from django.shortcuts import render
from courses.models import Course, Lesson


def index(request):
    course = Course.objects.all()
    return render(request, 'index.html', {'course': course})


def contact(request):
    return render(request, 'contact.html')


def student_list(request):
    return render(request, 'student_list.html')


def student_detail(request):
    return render(request, 'student_detail.html')

