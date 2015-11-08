# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='tweet',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='country',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='HashTag',
        ),
    ]
