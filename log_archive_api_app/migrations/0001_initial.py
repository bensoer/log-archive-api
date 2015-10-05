# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('appname', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
