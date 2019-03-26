from django.shortcuts import render
from django.views.generic import View,TemplateView,RedirectView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import UserSignupForm


# Create your views here.

class SignUpView(TemplateView):
	template_name="user/signup.html"

	def get(self,request):
		form=UserSignupForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form=UserSignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			username = request.POST.get('username')
			password = request.POST.get('password')
			login(request,user)
			return HttpResponseRedirect('/user/home')
		return render(request,self.template_name,{'form':form})


class LoginView(TemplateView):
	template_name='user/login.html'

	def post(self,request):
		username=request.POST.get('username')
		password=request.POST.get('password')
		print("login")
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect('/user/home')
		return render(request,self.template_name)


class Logout(LoginRequiredMixin,RedirectView):
	url='login/'

	def get(self,request):
		auth_logout(request)
		return HttpResponseRedirect('/')































