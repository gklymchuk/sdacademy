from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy, reverse
from courses.models import Course
from courses.forms import LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class CourseDetailView(DetailView):

    model = Course
    template_name = 'courses/detail.html'


class CourseCreateView(SuccessMessageMixin, CreateView):

    model = Course
    template_name = 'courses/add.html'
    success_message = 'Course %(name)s has been successfully added.'

    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Course creation'
        return context


class CourseUpdateView(SuccessMessageMixin, UpdateView):

    model = Course
    template_name = 'courses/edit.html'
    success_message = 'The changes have been saved.'

    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def get_success_url(self):
        return reverse('courses:edit', args=(self.object.pk,))


class CourseDeleteView(DeleteView):

    model = Course
    success_url = reverse_lazy('index')
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        course = self.get_object()
        messages.success(self.request, 'Course %s has been deleted.' % course.name)
        return super(CourseDeleteView, self).delete(request, *args, **kwargs)


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
