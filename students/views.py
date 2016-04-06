from students.models import Student
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin


class StudentListView(ListView):

    model = Student
    paginate_by = 2

    def get_queryset(self):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students

    def get_context_data(self, **kwargs):
        course_id = self.request.GET.get('course_id', None)
        context = super(StudentListView, self).get_context_data(**kwargs)
        if course_id:
            context['var'] = '&course_id=%s' % course_id
        return context


class StudentDetailView(DetailView):

    model = Student


class StudentCreateView(SuccessMessageMixin, CreateView):

    model = Student
    success_url = reverse_lazy('students:list_view')
    success_message = 'Student %(name)s %(surname)s has been successfully added'

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context


class StudentUpdateView(SuccessMessageMixin, UpdateView):

    model = Student
    success_message = 'Info on the student has been successfully changed.'

    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Student info update'
        return context

    def get_success_url(self):
        return reverse('students:edit', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):

    model = Student
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        messages.success(self.request, 'Info on %s %s has been successfully deleted.'
                         % (student.name, student.surname))
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)


