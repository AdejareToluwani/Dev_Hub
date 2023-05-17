from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.Home, name='h'),
    path('register', views.Signup, name='r'),
    path('profile', views.Profile, name='p'),
    path('profile_form', views.U_form, name='p_form'),
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='l')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
