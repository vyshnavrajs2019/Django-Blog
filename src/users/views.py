from django.shortcuts import render, redirect, reverse
from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
	if request.user.is_authenticated:
		return redirect(reverse('post:home'))
	form = LoginForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(request, email=email, password=password)
			if user:
				login(request, user)
				next_url = request.GET.get('next')
				if next_url:
					return redirect(next_url)
				return redirect(reverse('post:home'))
	context = {
		'form': form
	}
	return render(request, 'users/login.html', context)


def register_view(request):
	if request.user.is_authenticated:
		return redirect(reverse('post:home'))
	form = RegistrationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {
		'form': form
	}
	return render(request, 'users/register.html', context)


def logout_view(request):
	if not request.user.is_authenticated:
		return redirect(reverse('post:home'))
	logout(request)
	return redirect(reverse('post:home'))