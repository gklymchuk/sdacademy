from django.db import models


class Course(models.Model):
    name = models.CharField(verbose_name=u'Course Name', max_length=250)
    short_description = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    subject = models.CharField(verbose_name=u'Lesson Subject', max_length=250)
    description = models.TextField()
    course = models.ForeignKey(Course)
    order = models.PositiveIntegerField()

    def __unicode__(self):
        return self.subject

