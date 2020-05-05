from django.db import models




class Advice(models.Model):
    description = models.CharField(max_length=10000, null=False)
    image = models.CharField(max_length=10000, null=False)
    title = models.CharField(max_length=1000, null=False)


