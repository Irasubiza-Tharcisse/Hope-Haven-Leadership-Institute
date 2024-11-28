from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Leadership_team,Announcements
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request):
  user_profile = request.user
  context={
    'user_profile':user_profile
  }
  return render(request,'profile.html',context)


def team_view(request):
  team_members = Leadership_team.objects.all()
  return render(request, 'team.html', {'leadership_team': team_members})



# announ lidt
def announcement_list_view(request):
  announcements = Announcements.objects.all()
  return render(request, 'announcement_list.html', {'announcements': announcements})

@login_required
def create_announcement_view(request):
  if request.method == 'POST':
      title = request.POST.get('title')
      description = request.POST.get('description')
      image = request.FILES.get('image')

      # Create a new announcement instance
      announcement = Announcements(title=title, description=description, image=image)
      announcement.save()

      return redirect('announcement_list')  # Redirect to a list of announcements or a success page

  return render(request, 'create_announcement.html')
