from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from users.models import User


class Post(models.Model):
	title = models.CharField(max_length=120, unique=True)
	content = models.TextField()
	posted_on = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(unique=True, max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	published = models.BooleanField(default=False)
	caption = models.CharField(max_length=120, blank=True, null=True)
	image = models.ImageField(upload_to='media', blank=True, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse("post:detail", kwargs={"slug": self.slug})
	
	def get_update_url(self):
		return reverse("post:update", kwargs={"slug": self.slug})
	
	def get_delete_url(self):
		return reverse("post:delete", kwargs={"slug": self.slug})

	def get_media_url(self):
		return reverse("post:media", kwargs={"slug": self.slug})


class PostComment(models.Model):
	content = models.TextField(max_length=500)
	commented_on = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return "COMMENT: " + self.post.title
	
	def get_update_url(self):
		return reverse("post:edit-comment", kwargs={"slug": self.post.slug, "pk": self.id})
	
	def get_delete_url(self):
		return reverse("post:delete-comment", kwargs={"slug": self.post.slug, "pk": self.id})