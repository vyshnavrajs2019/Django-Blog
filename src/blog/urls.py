from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
    path('profile/', include('profiles.urls')),
	path('', users_views.register_view, name='register'),
	path('login/', users_views.login_view, name='login'),
	path('logout/', users_views.logout_view, name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
