from django.db import models
from django.contrib.auth.models import User


class Coach(models.Model):

    user = models.OneToOneField(User)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=250, choices=(('M', 'Male'), ('F', 'Female')))
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    description = models.TextField()

    def __unicode__(self):
        return self.user.first_name

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def is_staff(self):
        return self.user.is_staff

    def email(self):
        return self.user.email

