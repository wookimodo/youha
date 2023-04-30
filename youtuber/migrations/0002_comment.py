# Generated by Django 4.2 on 2023-04-30 09:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('youtuber', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videoId', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=100)),
                ('comment', models.TextField(default=None)),
                ('sentiment', models.CharField(default='', max_length=30)),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('date', models.CharField(default='', max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtuber.youtuber')),
            ],
        ),
    ]
