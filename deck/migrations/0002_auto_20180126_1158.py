# Generated by Django 2.0 on 2018-01-26 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]