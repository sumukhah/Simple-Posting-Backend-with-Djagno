from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponseRedirect
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
			form.save()
			return HttpResponseRedirect('/user/home')
		return render(request,self.template_name,{'form':form})
