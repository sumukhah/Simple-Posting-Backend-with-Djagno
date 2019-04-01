from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	profile_pic = models.ImageField(blank=True)
	date_of_birth=models.DateField(null=True,blank=True)
	phone_num=models.IntegerField(null=True,blank=True)

	def __str__(self):
		return self.user.username

class Post_Model(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.TextField(blank=True,null=True)
	content=models.TextField()

	def __str__(self):
		return self.title
