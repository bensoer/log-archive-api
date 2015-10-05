from django.db import models

# Create your models here.

class LogEntry(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    appname = models.TextField()
    message = models.TextField()