# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardTypeAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='deck',
            field=models.ManyToManyField(related_name='deck', to='deck.Card'),
        ),
        migrations.AlterField(
            model_name='player',
            name='hand',
            field=models.ManyToManyField(related_name='hand', to='deck.Card'),
        ),
    ]
