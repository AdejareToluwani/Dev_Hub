from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home', views.Home, name='h')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
