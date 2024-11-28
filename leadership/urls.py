from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from .views import team_view,create_announcement_view,announcement_list_view,profile_view

urlpatterns = [
  path('profile',profile_view,name='profile'),
  path('team/', team_view, name='team') ,
  path('announcement/', create_announcement_view, name='announcement'),
  path('announcement_list/', announcement_list_view, name='announcement_list')
]