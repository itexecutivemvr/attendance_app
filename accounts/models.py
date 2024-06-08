from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Log(models.Model):
    username = models.CharField(max_length=150)
    current_time = models.TimeField(default=timezone.now)
    current_date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.current_date} {self.current_time} - {self.location}"