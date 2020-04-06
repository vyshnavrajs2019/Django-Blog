from django.urls import path
from . import views

app_name = 'profiles'
urlpatterns = [
	path('<str:email>/', views.profile_home, name='home'),
	path('<str:email>/update/photo', views.photo_update, name='update-photo'),
	path('<str:email>/update/password', views.password_update, name='update-password'),
]
