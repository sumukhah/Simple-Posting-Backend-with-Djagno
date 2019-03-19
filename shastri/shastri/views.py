from django.shortcuts import render
from django.views.generic import View,TemplateView

def Home(request):
	return render(request,'home.html')

class UserHome(TemplateView):
	template_name='userhome.html'
