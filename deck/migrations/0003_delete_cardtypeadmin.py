# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0002_auto_20171214_1634'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CardTypeAdmin',
        ),
    ]
