# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
