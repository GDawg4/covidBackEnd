from rest_framework import serializers
from department.models import Department
from municipality.models import Municipality

class DepartmentSerializer(serializers.ModelSerializer):
    municipalities = serializers.PrimaryKeyRelatedField(many=True, queryset=Municipality.objects.all())

    class Meta:
        model = Department
        fields = (
            'departament_code',
            'name',
            'municipalities'
        )