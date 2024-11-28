from django.db import models
from django.contrib.auth.models import User



class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role_m = models.CharField(max_length=50)  # New field added
    photo = models.ImageField(upload_to='profile_photos', blank=True, null=True)
    def __str__(self):
        return f'{self.user.username}'

# Create your models here.
class Leadership_team(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='leadership_team/')

    def __str__(self):
        return f"{self.name}"
        # Customize the display

class Announcements(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='announcements/')

    def __str__(self):
        return f"{self.title}"
