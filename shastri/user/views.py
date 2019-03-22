from django.shortcuts import render
from django.views.generic import View,TemplateView,RedirectView
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from .forms import UserSignupForm,UserSignupCustomForm


# Create your views here.

class SignUpView(TemplateView):
	template_name="user/signup.html"

	def get(self,request):
		form=UserSignupForm()
		form2=UserSignupCustomForm()
		return render(request,self.template_name,{'form':form ,'form2':form2})

	def post(self,request):
		form=UserSignupForm(request.POST)
		form2=UserSignupCustomForm(request.POST)
		if form.is_valid() and form2.is_valid():
			form.save()
			username = request.POST.get('username')
			password = request.POST.get('password')
			form2.user=username
			form2.save()
			new_user=authenticate(username=username,password=password)
			login(request,new_user)
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
			print("login")

			return HttpResponseRedirect('/user/home')

		return render(request,self.template_name)


class Logout(LoginRequiredMixin,RedirectView):
	url='login/'

	def get(self,request):
		auth_logout(request)
		return HttpResponseRedirect('/')































