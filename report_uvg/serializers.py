from rest_framework import serializers

from user.models import User
from report_uvg.models import Report_uvg

class SelfReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report_uvg
        fields = (
            'id',
            'contagion_covid',
            'contagion_covid_days,'
            'cough',
            'day',
            'degrees_thermometer',
            'diarrhea',
            'difficulty_breathing',
            'fever',
            'sore_throat',
            'thermometer_temperature',
            'threw_up',
            'transmission_oms',
            'transmission_oms_days',
            'user'
        )