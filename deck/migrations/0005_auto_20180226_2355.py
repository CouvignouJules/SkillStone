# Generated by Django 2.0 on 2018-02-26 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0004_auto_20180225_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cardtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='deck.Cardtype'),
        ),
    ]
