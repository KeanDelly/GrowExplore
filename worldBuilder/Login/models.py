from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import datetime, timedelta

class CustomUser(AbstractUser):
    class Meta:
        managed = True
        db_table = 'Login_user'
    login_streak = models.IntegerField(default = 0)

    Harrison_Streak = models.IntegerField(default = 0)
    Harrison_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Amory_Streak = models.IntegerField(default = 0)
    Amory_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Forum_Streak = models.IntegerField(default = 0)
    Forum_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Business_Streak = models.IntegerField(default = 0)
    Business_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Cornwall_Streak = models.IntegerField(default = 0)
    Cornwall_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Northcott_Streak = models.IntegerField(default = 0)
    Northcott_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Geoffrey_Streak = models.IntegerField(default = 0)
    Geoffrey_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    GreatHall_Streak = models.IntegerField(default = 0)
    GreatHall_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Hatherly_Streak = models.IntegerField(default = 0)
    Hatherly_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Henry_Streak = models.IntegerField(default = 0)
    Henry_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Innovation_One_Streak = models.IntegerField(default = 0)
    Innovation_One_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Iais_Streak = models.IntegerField(default = 0)
    Iais_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Into_Streak = models.IntegerField(default = 0)
    into_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Laver_Streak = models.IntegerField(default = 0)
    Laver_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Library_Streak = models.IntegerField(default = 0)
    Library_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Living_Streak = models.IntegerField(default = 0)
    Living_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Mary_Streak = models.IntegerField(default = 0)
    Mary_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Old_Library_Streak = models.IntegerField(default = 0)
    Old_Library_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Peter_Streak = models.IntegerField(default = 0)
    Peter_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Physics_Streak = models.IntegerField(default = 0)
    Physics_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Queens_Streak = models.IntegerField(default = 0)
    Queen_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Reed_Streak = models.IntegerField(default = 0)
    Reed_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Wellbeing_Streak = models.IntegerField(default = 0)
    Wellbeing_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Mood_Streak = models.IntegerField(default = 0)
    Mood_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Sports_Streak = models.IntegerField(default = 0)
    Sports_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Streatham_Streak = models.IntegerField(default = 0)
    Streatham_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Health_Streak = models.IntegerField(default = 0)
    Health_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Washington_Streak = models.IntegerField(default = 0)
    Washington_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    Xfi_Streak = models.IntegerField(default = 0)
    Xfi_lastLogin = models.DateField(default = datetime.today()- timedelta(days = 1))

    UserRewards = models.CharField(default = "", max_length = 1024)

