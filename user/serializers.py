from rest_framework import serializers

from user.models import User
from report_uvg.models import Report_uvg
from report_housemates.models import report_housemates

class UserSerializer(serializers.ModelSerializer):
    reports_self = serializers.PrimaryKeyRelatedField(many=True, queryset=Report_uvg.objects.all())
    reports_other = serializers.PrimaryKeyRelatedField(many=True, queryset=report_housemates.objects.all())

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'useruvg',
            'content',
            'could_be_sick',
            'reports_self',
            'reports_other'
        )
