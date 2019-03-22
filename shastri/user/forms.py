from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserInfo


class UserSignupForm(UserCreationForm):
	first_name=forms.CharField(required=False,help_text='Optional.')
	email = forms.EmailField(max_length=50)
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

	class Meta:
		model = User
		fields = ('username','email',)

class UserSignupCustomForm(forms.ModelForm):
	profile_pic = forms.ImageField(required=False)
	date_of_birth=forms.DateField(required=False)
	phone_num=forms.IntegerField(required=False)


	class Meta:		
		model=UserInfo
		fields=['profile_pic','date_of_birth','phone_num']
	