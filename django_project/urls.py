
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views import index_view, about_view, contact_view, error_view, loginform_view, contactF,logout_user




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('404/', error_view, name='404'),

    # contact form
    path('contactF/', contactF, name='contactF'),
    # login form
    path('loginform/', loginform_view, name='loginform'),
    path('logout/', logout_user, name='logout'),

    path('',include('Blogs.urls')),
    
    path('',include('leadership.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
