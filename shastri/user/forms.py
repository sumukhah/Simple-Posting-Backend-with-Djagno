from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class UserSignupForm(UserCreationForm):
	first_name=forms.CharField(required=False,help_text='Optional.')
	email = forms.EmailField(max_length=50)
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')

	class Meta:
		model = User
		fields = ('username','email',)

	