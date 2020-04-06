from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Post, PostComment
from .forms import PostForm, PostCommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from django.views.generic import ListView
from .decorators import (
	only_post_created_user_has_access,
	only_post_comment_created_user_has_access
)


def search_view(request):
	query = request.GET.get('q')
	if not query:
		return redirect(reverse('post:home'))	
	posts = Post.objects.filter(
		Q(title__icontains=query)   |
		Q(content__icontains=query) |
		Q(author__email__contains=query)
	)
	context = {}
	context['posts'] = posts
	return render(request, 'post/list.html', context)

class PostListView(ListView):
	model = Post
	context_object_name = 'posts'

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	form = PostCommentForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		comment = form.save(commit=False)
		comment.post = post
		comment.user = request.user
		comment.save()
		return redirect(reverse('post:detail', kwargs={'slug': slug}))
	comments = post.comments.all()
	context = {}
	context['post'] = post
	context['form'] = form
	context['comments'] = comments
	return render(request, 'post/post_detail.html', context)


@login_required
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
	if request.method == 'POST' and form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.save()
		return redirect(reverse('post:detail', kwargs={'slug': post.slug}))
	context = {}
	context['form'] = form
	return render(request, 'post/create.html', context)


@login_required
@only_post_created_user_has_access
def post_update(request, slug, *args, **kwargs):
	post = kwargs.get('post')
	form = PostForm(request.POST or None, request.FILES or None, instance=post)
	if request.method == 'POST' and form.is_valid():
		post = form.save()
		return redirect(reverse('post:detail', kwargs={'slug': post.slug}))
	context = {}
	context['form'] = form
	return render(request, 'post/post_update.html', context)


@login_required
@only_post_created_user_has_access
def post_delete(request, slug, *args, **kwargs):
	post = kwargs.get('post')
	if request.method == 'POST':
		post.delete()
		return redirect(reverse('post:home'))
	context = {}
	context['post'] = post
	return render(request, 'post/post_confirm_delete.html', context)


@login_required
@only_post_comment_created_user_has_access
def post_comment_edit(request, slug, pk, *args, **kwargs):
	comment = kwargs.get('comment')
	form = PostCommentForm(request.POST or None, instance=comment)
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect(reverse('post:detail', kwargs={'slug': slug}))
	context = {}
	context['form'] = form
	context['comment'] = comment
	return render(request, 'post/comment_update.html', context)


@login_required
@only_post_comment_created_user_has_access
def post_comment_delete(request, slug, pk, *args, **kwargs):
	if request.method == 'POST':
		comment.delete()
		return redirect(reverse('post:detail', kwargs={'slug': slug}))
	context = {}
	context['comment'] = kwargs.get('comment')
	return render(request, 'post/comment_confirm_delete.html', context)