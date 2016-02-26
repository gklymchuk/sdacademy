# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Address'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(verbose_name='Birthday'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=75, verbose_name='Email'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=25, verbose_name='Phone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='skype',
            field=models.CharField(max_length=250, verbose_name='Skype'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=250, verbose_name='Surname'),
            preserve_default=True,
        ),
    ]
