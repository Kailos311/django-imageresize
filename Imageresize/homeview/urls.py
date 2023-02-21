from django.urls import path, include
from . import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', views.Home, name='Home'),
    path('upload', views.upload, name='Upload'),
    path('saveimage', views.Save, name='saveimage'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import *
  
# urlpatterns = [
#     path('image_upload/', avatarView, name = 'image_upload'),
#     path('success/', uploadok, name = 'success'),
# ]
  
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)