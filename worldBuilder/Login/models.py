from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    class Meta:
        managed = True
        db_table = 'Login_user'
    login_streak = models.IntegerField(default = 0)
    Harrison_Streak = models.IntegerField(default = 0)