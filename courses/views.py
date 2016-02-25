from django.shortcuts import render
from courses.models import Course, Lesson


def detail(request, crs_id):
    course_name = int(crs_id)
    course = Course.objects.get(id=course_name)
    lessons = Lesson.objects.filter(course=course_name)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})
