from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    useruvg = models.CharField(max_length=100)
    consent = models.BooleanField()

    def __str__(self):
        return 'User: {}'.format(self.name)
