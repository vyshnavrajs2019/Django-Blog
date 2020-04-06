from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
	path('', views.PostListView.as_view(), name='home'),
	path('new/', views.post_create, name='create'),
	path('search/', views.search_view, name='search'),
	path('<slug:slug>/', views.post_detail, name='detail'),
	path('<slug:slug>/update', views.post_update, name='update'),
	path('<slug:slug>/delete', views.post_delete, name='delete'),
	path('<slug:slug>/comment/<int:pk>/update', views.post_comment_edit, name='edit-comment'),
	path('<slug:slug>/comment/<int:pk>/delete', views.post_comment_delete, name='delete-comment'),
]
