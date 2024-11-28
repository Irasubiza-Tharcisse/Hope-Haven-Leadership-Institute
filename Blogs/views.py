from django.shortcuts import render
from .models import activities,testimonial
# Create your views here.

def activities_view(request):
  testimonial_members = testimonial.objects.all()
  all_activities = activities.objects.all()
  context = {'testimonial': testimonial_members, 'activities': all_activities}
  return render(request, 'activities.html', context)

def testimonial_view(request):
  testimonial_members = testimonial.objects.all()
  return render(request, 'testimonial.html',
                {'testimonial': testimonial_members})
