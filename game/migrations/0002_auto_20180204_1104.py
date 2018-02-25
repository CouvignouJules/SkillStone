# Generated by Django 2.0 on 2018-02-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameplayer',
            name='board',
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='board',
            field=models.TextField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='gameplayer',
            name='deck',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.RemoveField(
            model_name='gameplayer',
            name='hand',
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='hand',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='gameplayer',
            name='name',
            field=models.CharField(default=None, max_length=30),
        ),
    ]