# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-07 15:00
from __future__ import unicode_literals

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
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('g_status', models.IntegerField(blank=True, default=1)),
                ('userdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=200)),
                ('i_description', models.TextField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(upload_to='media/images')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('p_status', models.IntegerField(blank=True, default=1)),
                ('gallery_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
        ),
        migrations.CreateModel(
            name='UserContinuation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phoneno', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=6)),
                ('dob', models.DateField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('u_status', models.IntegerField(blank=True, default=1)),
                ('userdata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]