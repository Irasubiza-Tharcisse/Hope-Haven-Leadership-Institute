from django.http.response import HttpResponse
from django.shortcuts import render, redirect


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


from leadership.models import Leadership_team
from contact_us.models import ContactForm
from Blogs.models import activities,testimonial
from leadership.views import profile_view



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




def error_view(request):
  return render(request, '404.html', status=404)



# lists available for admin



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

def loginform_view(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        user = User.objects.filter(email=email).first()
   
        if user is not None and user.check_password(password): 
          login(request, user)
          
          return redirect(profile_view)
        else:
          messages.error(request, 'Invalid email or password')
          return redirect(loginform_view)
    except Exception as e:
        messages.error(request, f'error: {e}')
        return redirect(loginform_view)
    
  return render(request, 'loginform.html')


# logout
def logout_user(request):
  logout(request)  # Log out the user
  messages.success(request, 'You are now logged out')
  return redirect('loginform')  # Redirect to the homepage or any other page

# announcement

