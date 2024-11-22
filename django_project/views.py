from django.http.response import HttpResponse
from django.shortcuts import render, redirect

<<<<<<< HEAD
=======
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

>>>>>>> 5f3ab9e (Hope Haven L weApp)
from leadership.models import Leadership_team, ContactForm
from Blogs.models import activities,testimonial


<<<<<<< HEAD
=======

>>>>>>> 5f3ab9e (Hope Haven L weApp)
def index_view(request):
  team_members = Leadership_team.objects.all()
  testimonial_members = testimonial.objects.all()
  all_activities = activities.objects.all()
  context = {
      'leadership_team': team_members,
      'testimonial': testimonial_members,
      'activities': all_activities,
  }
  return render(request, 'index.html', context)


def about_view(request):
  team_members = Leadership_team.objects.all()
  return render(request, 'about.html', {'leadership_team': team_members})


def contact_view(request):
  return render(request, 'contact.html')


def activities_view(request):
  testimonial_members = testimonial.objects.all()
  all_activities = activities.objects.all()
  context = {'testimonial': testimonial_members, 'activities': all_activities}
  return render(request, 'activities.html', context)


def team_view(request):
  team_members = Leadership_team.objects.all()
  return render(request, 'team.html', {'leadership_team': team_members})


def error_view(request):
  return render(request, '404.html')


def testimonial_view(request):
  testimonial_members = testimonial.objects.all()
  return render(request, 'testimonial.html',
                {'testimonial': testimonial_members})


# lists available for admin


def teamList_view(request):
  team_members = Leadership_team.objects.all()
  return render(request, 'teamList.html', {'leadership_team': team_members})


def testimonialList_view(request):
  testimonial_members = testimonial.objects.all()
  return render(request, 'testimonial_List.html',
                {'testimonial': testimonial_members})


def contactF(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    class_name = request.POST.get('class_name')
    message = request.POST.get('message')
    contact = ContactForm(name=name,
                                         email=email,
                                         class_name=class_name,
                                         message=message)
    contact.save()
    return redirect(contact_view)
  return redirect(index_view)
<<<<<<< HEAD
=======

def loginform_view(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect(loginform_view)
    else:
      messages.error(request, 'Invalid email or password')
      return redirect(loginform_view)return redirect(loginform_view)
  return render(request, 'loginform.html')
>>>>>>> 5f3ab9e (Hope Haven L weApp)
