# Model

# from django.db import models

# # Create your models here.
# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class CustomUser(AbstractUser):
# 	username=None
# 	email = models.EmailField(unique=True)

# 	USERNAME_FIELDS = "email"

# 	def __str__(self):
# 		return self.email


# Forms

# from django.contrib.auth.forms import UserCreationForm,UserChangeForm
# from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('username', 'email','password')


# Admin

# from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm
# from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     model = CustomUser
#     list_display = ['email', 'username',]

# admin.site.register(CustomUser, CustomUserAdmin)
