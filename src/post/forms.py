from django import forms
from .models import Post, PostComment

class PostForm(forms.ModelForm):
	title = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'autocomplete': 'off',
				'placeholder': 'Title', 
				'class': 'input input-sm p-1'
			}
		)
	)
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Content', 
				'class': 'textarea textarea-lg p-1'
			}
		)
	)
	published = forms.BooleanField(
		required=False,
		label='Publish',
		widget=forms.CheckboxInput()
	)
	caption = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
				'autocomplete': 'off',
				'placeholder': 'Caption', 
				'class': 'input input-sm p-1'
			}
		)
	)
	image = forms.ImageField(
		required=False
	)

	class Meta:
		model = Post
		fields = [
			'title',
			'caption',
			'image',
			'content',
			'published',
		]

class PostCommentForm(forms.ModelForm):
	content = forms.CharField(
		widget=forms.Textarea(
			attrs={
				'placeholder': 'Your comment',
				'class': 'textarea textarea-md p-1'
			}
		)
	)

	class Meta:
		model = PostComment
		fields = [
			'content',
		]