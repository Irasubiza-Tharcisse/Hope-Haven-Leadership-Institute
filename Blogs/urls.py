from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.resolvers import URLPattern
from .views import activities_view, testimonial_view

urlpatterns =[

  path('activities/', activities_view, name="activities"),
  path('testimonial/', testimonial_view, name="testimonial"),
  
]
