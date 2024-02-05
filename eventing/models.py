from django.db import models
from accounts.models import Users

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    dateday = models.DateTimeField()
    start_hour = models.TimeField(null=True)
    end_hour = models.TimeField(null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


