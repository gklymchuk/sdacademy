from django.shortcuts import render, redirect
from students.models import Student
from students.forms import StudentModelForm
from django.contrib import messages


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


def create(request):
    form = StudentModelForm
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            form.save()
            messages.success(request, 'Student %s %s has been successfully added' % (name, surname))
            return redirect('students:list_view')
    return render(request, 'students/add.html', {'form': form})


def edit(request, pk):
    pk = int(pk)
    student = Student.objects.get(pk=pk)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            print request.POST
            form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    return render(request, 'students/edit.html', {'form': form})


def remove(request, pk):
    pk = int(pk)
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        return redirect('students:list_view')
    return render(request, 'students/remove.html', {'student': student})
