# Generated by Django 2.0 on 2018-02-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20180204_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplayer',
            name='board',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
