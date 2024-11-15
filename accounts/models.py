from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Users(AbstractUser):
    is_active = models.BooleanField(default=False)
    email = models.EmailField(blank=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex],max_length=17)