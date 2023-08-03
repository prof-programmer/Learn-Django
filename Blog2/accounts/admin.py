from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 		#adminlarni klassi
from .forms import CustomUserCreationForm, CustomUserChangeForm 	#formalarni chaqiryapmiz
from .models import CustomUser 							#modellarni ham chaqirish kerak ekan

# Register your models here.


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm 	#foydalanuvchi qoshish
	form = CustomUserChangeForm			#foydalanuvchini ozgartirish
	model = CustomUser 					#biz foydalanadigan model			

admin.site.register(CustomUser, CustomUserAdmin)	#shu kod orqali biz qoshgan yangi modellar admin panelda korinadi




























































