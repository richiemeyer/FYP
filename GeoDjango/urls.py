from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.urls import include, path
from world import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('updatedb/', user_views.update_location, name='updatedb'),
    # URL path to get the last journey
    path('getLastJourney/', user_views.get_last_journey, name='getLastJourney'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('world.urls')),
    url('', include('pwa.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


