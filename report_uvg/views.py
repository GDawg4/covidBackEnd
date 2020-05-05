from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from report_uvg.models import Report_uvg
from report_uvg.serializers import SelfReportSerializer

# Create your views here.








@action(detail=True, methods=['get'])
def reports_uvg(self, request, pk=None):
    reports_uvg = self.get_object()
    response = []
    for report_uvg in reports_uvg.object.all():
        response.append(report_uvg)

    return Response(response)
    
