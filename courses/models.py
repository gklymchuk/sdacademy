from django.db import models
from coaches.models import Coach
from django.core.urlresolvers import reverse


class Course(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=250)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    coach = models.ForeignKey(Coach, null=True, blank=True, related_name='coach_courses')
    assistant = models.ForeignKey(Coach, null=True, blank=True, related_name='assistant_courses')

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index')


class Lesson(models.Model):
    subject = models.CharField(verbose_name=u'Subject', max_length=250)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject


