# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=250)),
                ('book', models.ForeignKey(related_name='book_purchase', to='book.Book')),
                ('user', models.ForeignKey(related_name='user_purchase', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
