from django.db import models

# Create your models here.
from django.db import models
import uuid

# Create your models here.
class report_housemates(models.Model):
    contagion_covid = models.BooleanField()
    contagion_covid_days = models.IntegerField()
    cough = models.BooleanField()
    day = models.DateField(auto_now_add=True)
    degrees_thermometer = models.IntegerField()
    diarrhea = models.BooleanField()
    difficulty_breathing = models.BooleanField()
    fever = models.BooleanField()
    sore_throat = models.BooleanField()
    thermometer_temperature = models.BooleanField()
    threw_up = models.BooleanField()
    transmission_oms = models.BooleanField()
    transmission_oms_days = models.BooleanField()
    reported_by = models.ForeignKey(
        'user.User',
        related_name='reports_other',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return 'Report: {}'.format(self.reported_by.name)