from django.db import models
from leadership.models import Leadership_team
# Create your models here.
class testimonial(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  description = models.TextField()
  image = models.ImageField(upload_to='testimonial/')

  def __str__(self):
      return f"{self.name}"


class activities(models.Model):
  option_A = 'All Student'
  option_B = 'All Staff'
  option_C = 'All Students and Staff'
  option_D = 'Some Students'
  choices = [(option_A, 'All Student'), (option_B, 'All Staff'),
             (option_C, 'All Students and Staff'),
             (option_D, 'Some Students')]
  assigned = models.CharField(max_length=100,
                              choices=choices,
                              default=option_A)
  description = models.CharField(max_length=100)
  supervisor = models.ForeignKey(Leadership_team, on_delete=models.CASCADE)
  time_range = models.CharField(max_length=100)
  needed = models.CharField(max_length=100, default='All students')
  image = models.ImageField(upload_to='activities/')

  def __str__(self):
      return f"{self.description}"