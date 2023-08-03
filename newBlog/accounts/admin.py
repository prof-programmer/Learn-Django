from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 		#adminlarni klassi
from .forms import CustomUserCreationForm, CustomUserChangeForm 	#formalarni chaqiryapmiz
from .models import CustomUser 							#modellarni ham chaqirish kerak ekan

# Register your models here.


class CustomUserAdmin(UserAdmin):
	add_form = CustomUserCreationForm 	#foydalanuvchi qoshish
	form = CustomUserChangeForm			#foydalanuvchini ozgartirish
	model = CustomUser 					#biz foydalanadigan model			
	list_display = ['email', 'username', 'first_name', 'last_name', 'age', 'is_staff']
	fieldsets = UserAdmin.fieldsets + (
		(None, {'fields': ('age',)}),
	)
	add_fieldsets = UserAdmin.add_fieldsets + (
		(None, {'fields': ('age',)}),
	)

admin.site.register(CustomUser, CustomUserAdmin)	#shu kod orqali biz qoshgan yangi modellar admin panelda korinadi




























































