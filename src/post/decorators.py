from django.utils.functional import wraps
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from .models import Post

def only_post_created_user_has_access(view_func):
	@wraps(view_func)
	def wrapper_function(request, slug, *args, **kwargs):
		post = get_object_or_404(Post, slug=slug)
		if request.user != post.author:
			raise PermissionDenied
		else:
			kwargs['post'] = post
			return view_func(request, slug, *args, **kwargs)
	return wrapper_function


def  only_post_comment_created_user_has_access(view_func):
	@wraps(view_func)
	def wrapper_function(request, slug, pk, *args, **kwargs):
		post = get_object_or_404(Post,slug=slug)
		post_comments = post.comments.all()
		comment = post_comments.filter(pk=pk).first()
		if not comment:
			raise Http404
		elif request.user != comment.user:
			raise PermissionDenied
		else:
			kwargs['comment'] = comment
			return view_func(request, slug, pk, *args, **kwargs)
	return wrapper_function