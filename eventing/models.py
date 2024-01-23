from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Users(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=17)

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    dateday = models.DateTimeField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


