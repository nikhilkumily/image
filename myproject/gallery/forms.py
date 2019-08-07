from .models import Gallery,Photos,UserContinuation
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class GalleryForm(forms.ModelForm):
	class Meta:
		model = Gallery
		exclude = ('userdata','created_on','g_status')

class ImageForm(forms.ModelForm):
	class Meta:
		model = Photos
		fields = ['i_name',
				'i_description',
				'gallery_name',
				'image']



class AddUserForm(forms.ModelForm):
	class Meta:
		model = UserContinuation
		fields = ['dob','phoneno','gender','u_status']
		

class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	class meta:
		model = User
		fields = ['username','password1','password2','first_name','last_name','email']








	