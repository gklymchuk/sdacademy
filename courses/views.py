from django.shortcuts import render, redirect
from courses.models import Course, Lesson
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, pk):
    course_name = int(pk)
    course = Course.objects.get(id=course_name)
    lessons = Lesson.objects.filter(course=course_name)
    return render(request, 'courses/detail.html', {'course': course, 'lessons': lessons})


def create(request):
    form = CourseModelForm
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            form.save()
            messages.success(request, 'Course %s has been successfully added.' % name)
            return redirect('index')
    return render(request, 'courses/add.html', {'form': form})


def edit(request, pk):
    pk = int(pk)
    course = Course.objects.get(pk=pk)
    form = CourseModelForm(instance=course)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'The changes have been saved.')
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, pk):
    pk = int(pk)
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course %s has been deleted.' % course.name)
        return redirect('index')
    return render(request, 'courses/remove.html', {'course': course})


def add_lesson(request, pk):
    course = Course.objects.get(pk=pk)
    form = LessonModelForm(initial={'course': course})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % subject)
            return redirect('courses:detail', pk=pk)
    return render(request, 'courses/add_lesson.html', {'form': form})
