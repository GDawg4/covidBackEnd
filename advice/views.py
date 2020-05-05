from django.shortcuts import render
from rest_framework import viewsets
from advice.serializers import AdviceSerializer
from advice.models import Advice

class AdviceViewSet(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer
