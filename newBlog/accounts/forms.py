from django.contrib.auth.forms import UserCreationForm, UserChangeForm # djangodagi tayyor klasslar import qilindi, foydalanuvchi reg va ozgartirish formalari
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'email', 'age',)