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
    first_name = User.objects.get().first_name
    last_name = User.objects.get().last_name

    def __unicode__(self):
        return self.first_name
