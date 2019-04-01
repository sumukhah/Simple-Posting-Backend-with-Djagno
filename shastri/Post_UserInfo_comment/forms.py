from django import forms
from .models import Post_Model


class PostForm(forms.ModelForm):
	title=forms.CharField(widget=forms.TextInput(attrs={'size': '20'}),label='Title')
	content=forms.TextInput()

	class Meta:
		model=Post_Model
		fields=('title','content')
