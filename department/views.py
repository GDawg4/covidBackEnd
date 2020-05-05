
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.core.exceptions import PermissionDenied

from advice.models import Advice
from municipality.models import Municipality
from report_housemates.models import Report_housemates
from report_uvg.models import Report_uvg
from user.models import User

from advice.serializers import AdviceSerializer
from municipality.serializers import MunicipalitySerializer
from report_housemates.serializers import Report_housematesSerializer
from report_uvg.serializers import Report_uvgSerializer
from user.serializers import UserSerializer

# Create your views here.
def evaluate_permission(user, obj, request):
    return user.first_name == obj.owner.name

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        print(user.username)

        department = serializer.save()
        assign_perm('departments.view_department', user, department)
    