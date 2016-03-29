from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    from_email = models.EmailField(verbose_name=u'Email')
    create_date = models.DateTimeField(auto_now_add=True)
