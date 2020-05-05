from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from municipality.models import Municipality
from municipality.serializers import MunicipalitiesSerializers

# Create your views here.
#End points
@action(detail=True, methods=['get'])
def municipalitys(self, request, pk=None):
    municipalitys = self.get_object()
    response = []
    for municipality in municipalitys.object.all():
        response.append(municipality)

    return Response(response)
    
