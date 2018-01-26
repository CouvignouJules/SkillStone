# Generated by Django 2.0 on 2018-01-26 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GamePlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('hp', models.IntegerField(default=30)),
                ('board', models.ManyToManyField(related_name='board', to='deck.Card')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.Deck')),
                ('hand', models.ManyToManyField(related_name='hand', to='deck.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playersHP', models.IntegerField(default=30)),
                ('startingHand', models.IntegerField(default=3)),
                ('spellUse', models.BooleanField(default=True)),
                ('monstersBoard', models.IntegerField(default=7)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='players',
            field=models.ManyToManyField(to='game.GamePlayer'),
        ),
    ]
