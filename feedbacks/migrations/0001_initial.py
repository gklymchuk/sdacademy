# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('subject', models.CharField(max_length=250, verbose_name='Name')),
                ('message', models.TextField()),
                ('from_email', models.EmailField(max_length=75, verbose_name='Email')),
                ('create_date', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
