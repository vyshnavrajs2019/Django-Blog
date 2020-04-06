from django.shortcuts import render, get_object_or_404, redirect, reverse
from users.models import User
from .models import Profile
from users.forms import UserPasswordChangeForm, PhotoChangeForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied


@login_required
def photo_update(request, email):
	user = get_object_or_404(User, email=email)
	if request.user != user:
		raise PermissionDenied
	form =  PhotoChangeForm(request.POST or None, request.FILES or None, instance=user)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect(reverse('profiles:home', kwargs={'email': email}))
			
	context = {
		'form': form
	}
	return render(request, 'profiles/photo.html', context)

@login_required
def password_update(request, email):
	user = get_object_or_404(User, email=email)
	if request.user != user:
		raise PermissionDenied
	form =  UserPasswordChangeForm(data=request.POST or None, user=user)
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			return redirect('login')
			
	context = {
		'form': form
	}
	return render(request, 'profiles/edit.html', context)

def profile_home(request, email):
	user = get_object_or_404(User, email=email)
	
	following = user.following
	followers = user.followers

	is_follower = request.user.following.filter(to_user=user).first() if request.user.is_authenticated else False
	if request.method == 'POST' and request.user.is_authenticated:
		if request.user != user:
			if not is_follower:
				profile = Profile.objects.create(
					from_user=request.user, 
					to_user=user
				)
			else:
				is_follower.delete()
			return redirect(reverse('profiles:home', kwargs={'email': email}))
	context = {
		'user': user,
		'is_follower': is_follower,
		'followers': followers.count(),
		'following': following.count()
	}
	return render(request, 'profiles/profile.html', context)
