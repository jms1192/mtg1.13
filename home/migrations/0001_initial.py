# Generated by Django 3.0.6 on 2020-05-19 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cost', models.CharField(max_length=100)),
                ('cmc', models.DecimalField(decimal_places=1, max_digits=5)),
                ('color', models.CharField(max_length=100)),
                ('type1', models.CharField(max_length=100)),
                ('sub_type', models.CharField(max_length=100)),
                ('supper_type', models.CharField(max_length=100)),
                ('sets', models.CharField(max_length=200)),
                ('rulestext', models.CharField(max_length=500)),
                ('flavor_text', models.CharField(max_length=500)),
                ('power', models.DecimalField(decimal_places=1, max_digits=5)),
                ('toughness', models.DecimalField(decimal_places=1, max_digits=5)),
                ('loyality', models.DecimalField(decimal_places=1, max_digits=5)),
                ('costusd', models.DecimalField(decimal_places=1, max_digits=5)),
                ('user_tag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='follow_modle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='home.UserProfile')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='home.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='decks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deck_name', models.CharField(max_length=100)),
                ('hash_tags', models.CharField(max_length=250)),
                ('deck_discription', models.CharField(max_length=500)),
                ('deck_views', models.PositiveIntegerField()),
                ('deck_copies', models.PositiveIntegerField()),
                ('deck_publish', models.BooleanField(default=False)),
                ('deck_type', models.CharField(default='nome', max_length=20)),
                ('date_publish', models.DateTimeField(auto_now=True)),
                ('deck_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='cards_in_deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cards')),
                ('deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.decks')),
            ],
        ),
    ]