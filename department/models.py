from django.db import models
import uuid

# Create your models here.
class Department(models.Model):
    departament_code = models.IntegerField(unique = True, null=True)
    name = models.IntegerField(blank=False, null=False, unique=True)
