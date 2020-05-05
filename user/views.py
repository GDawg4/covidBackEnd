from django.shortcuts import render
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from django.core.exceptions import PermissionDenied

from advice.models import Advice
from department.models import Department
from municipality.models import Municipality
from report_housemates.models import report_housemates
from report_uvg.models import Report_uvg
from user.models import User

from advice.serializers import AdviceSerializer
# from municipality.serializers import MunicipalitySerializer
# from report_housemates.serializers import Report_housematesSerializer
# from report_uvg.serializers import Report_uvgSerializer
from user.serializers import UserSerializer

def evaluate_permission(user, obj, request):
    return user.first_name == obj.owner.name

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @action(detail=True, url_path='departments', methods=['get'])
  def viewDepartments(self, request, pk=None):
    user = self.get_object()
    if(user.name == self.request.user.name):
      department_list = Department.objects.filter(user = user)
      response = DepartmentSerializer(department_list, many = True).data
      return Response(response)
    else:
      raise PermissionDenied()

  @action(detail=True, url_path='municipalities', methods=['get'])
  def viewMunicipalities(self, request, pk=None):
    user = self.get_object()
    if(user.name == self.request.user.name):
      municipality_list = municipalities.objects.filter(user = user)
      response = municipalitiesSerializer(municipality_list, many = True).data
      return Response(response)
    else:
      raise PermissionDenied()