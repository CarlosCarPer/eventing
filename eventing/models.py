from django.db import models
from accounts.models import Users

class Events(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    dateday = models.DateTimeField()
    start_hour = models.TimeField(null=True)
    end_hour = models.TimeField(null=True)
    author = models.ForeignKey(Users, related_name='my_events', on_delete=models.CASCADE)
    members = models.ManyToManyField(Users,related_name='events')

    def __str__(self):
        return self.title

class Tasks(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    event = models.ForeignKey(Events,related_name='tasks',on_delete=models.CASCADE)
    members = models.ManyToManyField(Users,related_name='members',blank=True)

    def __str__(self):
        return self.title