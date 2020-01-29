from .models import Race
from rest_framework import serializers


class RaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Race
        fields = ['name']
