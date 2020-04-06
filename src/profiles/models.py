from django.db import models
from users.models import User

class Profile(models.Model):
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
	to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
	following_since = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.from_user.first_name} {self.from_user.last_name}  -> {self.to_user.first_name} {self.to_user.last_name}'
	