# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gallery(models.Model):
	# g_id = models.IntegerField()
	userdata = models.ForeignKey(User, on_delete=models.CASCADE)
	g_name = models.CharField(max_length=200)
	description = models.TextField(max_length=200,blank=True,null=True)
	created_on = models.DateTimeField(auto_now=True)
	g_status = models.IntegerField(default=1,blank=True)
	def __str__(self):
		return self.g_name


class Photos(models.Model):
	# i_id = models.IntegerField()
	i_name = models.CharField(max_length=200)
	i_description = models.TextField(max_length=200,blank=True,null=True)
	gallery_name = models.ForeignKey(Gallery ,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='media/images' , blank=True, null=True)
	created_on = models.DateTimeField(auto_now=True)
	p_status = models.IntegerField(default=1,blank=True)
	def __str__(self):
		return self.i_name

class UserContinuation(models.Model):
	userdata = models.OneToOneField(User, on_delete=models.CASCADE)
	# address=models.TextField(max_length=200)
	phoneno = models.IntegerField()
	gender_choice =(
		('Male','Male'),
		('Female','Female')
		)
	gender = models.CharField(max_length=6,choices=gender_choice,default=1)
	# image=models.ImageField(upload_to='media/images')
	dob=models.DateField()
	created_on=models.DateTimeField(auto_now=True)
	u_status = models.IntegerField(default=1,blank=True)
	def __str__(self):
		return self.userdata.username