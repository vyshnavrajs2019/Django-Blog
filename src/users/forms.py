from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	email = forms.EmailField(
		max_length=30, 
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'input input-sm p-1'
			}
		)
	)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'input input-sm p-1'
			}
		)
	)

	def clean(self):
		email = self.cleaned_data.get('email')
		password = self.cleaned_data.get('password')
		if not authenticate(email=email, password=password):
			raise forms.ValidationError("Invalid Login")

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(
		max_length=30, 
		widget=forms.EmailInput(
			attrs={
				'placeholder': 'Email',
				'class': 'input input-sm p-1'
			}
		)
	)
	password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Password',
				'class': 'input input-sm p-1'
			}
		)
	)
	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm Password',
				'class': 'input input-sm p-1'
			}
		)
	)
	first_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder': 'First Name',
				'class': 'input input-sm p-1'
			}
		)
	)
	last_name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Last Name',
				'class': 'input input-sm p-1'
			}
		)
	)

	class Meta:
		model = User
		fields = [
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2'
		]

class UserPasswordChangeForm(PasswordChangeForm):
	new_password1 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'New Password',
				'class': 'input input-sm p-1'
			}
		)
	)
	new_password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Confirm New Password',
				'class': 'input input-sm p-1'
			}
		)
	)
	old_password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder': 'Old Password',
				'class': 'input input-sm p-1'
			}
		)
	)
	class Meta:
		model = User
		fields = [
			'new_password1',
			'new_password2',
			'old_password'
		]


class PhotoChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['profile_pic']