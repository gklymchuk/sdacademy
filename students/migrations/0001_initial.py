# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name="Student's Name")),
                ('surname', models.CharField(max_length=250, verbose_name="Student's Surname")),
                ('date_of_birth', models.DateField(verbose_name="Student's Birthday")),
                ('email', models.EmailField(max_length=75, verbose_name="Student's Email")),
                ('phone', models.CharField(max_length=25, verbose_name="Student's Phone")),
                ('address', models.CharField(max_length=250, verbose_name="Student's Address")),
                ('skype', models.CharField(max_length=250, verbose_name="Student's Skype")),
                ('courses', models.ManyToManyField(to='courses.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
