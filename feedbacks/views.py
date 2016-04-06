from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from sdacademy import settings
from django.core.urlresolvers import reverse_lazy


class FeedbackView(SuccessMessageMixin, CreateView):

    model = Feedback
    template_name = 'feedback.html'
    success_message = 'Thank you for your feedback! We will keep in touch with you very soon!'
    success_url = reverse_lazy('feedback')
    contacts = [i[1] for i in settings.ADMINS]

    def form_valid(self, form):
        data = form.cleaned_data
        send_mail(data['subject'], data['message'], data['from_email'], self.contacts, fail_silently=False)
        return super(FeedbackView, self).form_valid(form)
