from rest_framework import serializers
from municipality.models import Municipality

class  MunicipalitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = (
            'municipality_code',
            'name',
            'dep_code'
        )