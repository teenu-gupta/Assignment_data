# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_auto_20190830_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetail',
            name='plan_name',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]
