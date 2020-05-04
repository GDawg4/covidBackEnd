from django.db import models
import uuid

# Create your models here.
class Department(models.Model):
    department_code = models.IntegerField(blank=False, null=False, unique=True)
    name = models.IntegerField(blank=False, null=False, unique=True)
