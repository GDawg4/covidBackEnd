from django.db import models
import uuid

# Create your models here.
class Municipality(models.Model):
    municipality_code = models.IntegerField(blank=False, null=False, unique=True)
    nombre = models.CharField(max_length=100)
    dep_code = models.ForeignKey(
        'department.Department',
        related_name='municipalities',
        on_delete=models.SET_NULL,
        null=True
    )