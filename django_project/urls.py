
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from .views import index_view, about_view, contact_view, activities_view, team_view, error_view, testimonial_view, teamList_view, testimonialList_view, contactF
=======
from .views import index_view, about_view, contact_view, activities_view, team_view, error_view, testimonial_view, teamList_view, testimonialList_view, contactF, loginform_view
>>>>>>> 5f3ab9e (Hope Haven L weApp)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name="index"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('activities/', activities_view, name="activities"),
    path('team/', team_view, name="team"),
    path('404/', error_view, name='404'),
    path('testimonial/', testimonial_view, name='testimonial'),
    # lists of different data
    path('teamList/', teamList_view, name='teamList'),
    path('testimonial_List/', testimonialList_view, name='testimonial_List'),
    # contact form
    path('contactF/', contactF, name='contactF'),
<<<<<<< HEAD
=======
    # login form
    path('loginform/', loginform_view, name='loginform'),
>>>>>>> 5f3ab9e (Hope Haven L weApp)
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
