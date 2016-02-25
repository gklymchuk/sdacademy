from django.db import models
from courses.models import Course


class Student(models.Model):
    name = models.CharField(verbose_name=u'Name', max_length=250)
    surname = models.CharField(verbose_name=u'Surname', max_length=250)
    date_of_birth = models.DateField(verbose_name=u'Birthday')
    email = models.EmailField(verbose_name=u'Email')
    phone = models.CharField(verbose_name=u'Phone', max_length=25)
    address = models.CharField(verbose_name=u'Address', max_length=250)
    skype = models.CharField(verbose_name=u'Skype', max_length=250)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.surname
