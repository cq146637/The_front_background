# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 10:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20170715_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='user_group',
        ),
    ]
