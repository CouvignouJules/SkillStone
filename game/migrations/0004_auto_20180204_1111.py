# Generated by Django 2.0 on 2018-02-04 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180204_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameplayer',
            name='board',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='gameplayer',
            name='deck',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='gameplayer',
            name='hand',
            field=models.TextField(default=None),
        ),
    ]
