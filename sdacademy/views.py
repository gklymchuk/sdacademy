from django.shortcuts import render
from courses.models import Course


def index(request):
    course = Course.objects.all()
    return render(request, 'index.html', {'course': course})


def contact(request):
    return render(request, 'contact.html')

