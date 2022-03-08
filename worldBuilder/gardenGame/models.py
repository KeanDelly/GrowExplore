from cProfile import label
import datetime
from django.db import models

# Create your models here.


# Database model for registering a building of the day
class buildingOfTheDay(models.Model):

    building_name = models.CharField(max_length=200)
    building_desc = models.CharField(max_length=200)
    date = models.DateField(default=datetime.date.today)
    reward = models.CharField(max_length=200)
