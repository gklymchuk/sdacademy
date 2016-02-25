from django.shortcuts import render
from students.models import Student


def detail(request, st_id):
    st_name = int(st_id)
    student = Student.objects.get(id=st_name)
    return render(request, 'students/detail.html', {'student': student})


def list_view(request):
    try:
        req = int(request.GET.get('course_id', '')[0])
        students = Student.objects.filter(courses=req)
        return render(request, 'students/list.html', {'students': students})
    except IndexError:
        students = Student.objects.all()
        return render(request, 'students/list.html', {'students': students})
