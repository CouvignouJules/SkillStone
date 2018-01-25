# Generated by Django 2.0 on 2018-01-12 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0005_auto_20180112_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='nom',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='card',
            name='effect',
        ),
        migrations.AddField(
            model_name='card',
            name='effect',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deck.Effect'),
        ),
    ]