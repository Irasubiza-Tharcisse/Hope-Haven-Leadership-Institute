from django.db import models


# Create your models here.
class Leadership_team(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='leadership_team/')

    def __str__(self):
        return f"{self.name}"
        # Customize the display


# contact form
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    class_name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
