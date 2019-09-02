# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_state', models.CharField(max_length=90, verbose_name='Account_state')),
                ('account_id', models.FloatField()),
                ('activated_at', models.DateField()),
                ('expires_at', models.DateTimeField(auto_now_add=True)),
                ('current_period_started_at', models.DateTimeField(auto_now_add=True)),
                ('current_period_ends_at', models.DateTimeField(auto_now_add=True)),
                ('plan_name', models.CharField(max_length=256)),
                ('business_id', models.IntegerField()),
                ('enterprise_id', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('category_id', models.IntegerField()),
                ('parent_category_name', models.CharField(max_length=256, verbose_name='Parent Category Name')),
                ('count', models.IntegerField()),
                ('avg_monthly_rating', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
