from django.shortcuts import render
from .forms import PostForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
from .models import UserInfo,Post_Model
from django.views.generic import ListView,DetailView,TemplateView

class UserHome(ListView):
	model=Post_Model
	context_object_name='post'
	template_name='Post_Userinfo_comment/list.html'


class CreatePost(TemplateView):
	template_name='base.html'
	
	def get(self,request):
		form=PostForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=PostForm(request.POST)
		if form.is_valid():
			form.author=request.user
			form.save()
			return HttpResponseRedirect('/user/home')
		return render(request,self.template_name)

