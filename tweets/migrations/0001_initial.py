# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('text', models.CharField(max_length=140)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('country', models.CharField(max_length=30, default='Global')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(to='user_profile.User')),
            ],
        ),
        migrations.AddField(
            model_name='hashtag',
            name='tweet',
            field=models.ManyToManyField(to='tweets.Tweet'),
        ),
    ]
