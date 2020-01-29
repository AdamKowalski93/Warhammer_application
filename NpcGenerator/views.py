from django.shortcuts import render
from .models import Race
from rest_framework import viewsets
from NpcGenerator.serializers import RaceSerializer


class RaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
