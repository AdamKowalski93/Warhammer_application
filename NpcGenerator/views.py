from django.shortcuts import render
from .models import Race,Class
from rest_framework import viewsets
from NpcGenerator.serializers import RaceSerializer,ClassSerializer


class RaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Race.objects.all()
    serializer_class = RaceSerializer

class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Class.objects.filter(race__name='Człowiek')
    serializer_class = ClassSerializer
