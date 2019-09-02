# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0002_auto_20190830_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessdetail',
            name='business_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='businessdetail',
            name='enterprise_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
