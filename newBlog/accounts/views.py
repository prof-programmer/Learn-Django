from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

# Create your views here.
class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')	#foydalanuvchi royxatdan o'tgandan keyin reverse_lazy orqali login sahifaga o'tadi
	template_name = 'registration/signup.html'