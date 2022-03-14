from cProfile import label
import datetime
from django.db import models

# Create your models here.




# Database model for registering a building of the day
class buildingOfTheDay(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    reward = models.CharField(max_length=200)

class reportToAdmin(models.Model):
    problem_name = models.CharField(max_length=200)
    problem_description = models.CharField(max_length=200)
    username = models.CharField(max_length=200, default='user')
    email = models.CharField(max_length=200, default='email')