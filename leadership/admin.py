from django.contrib import admin
from .models import ContactForm, Leadership_team
from Blogs.models import activities, testimonial
# Register your models here.
admin.site.register(Leadership_team)
admin.site.register(testimonial)
admin.site.register(activities)
admin.site.register(ContactForm)
