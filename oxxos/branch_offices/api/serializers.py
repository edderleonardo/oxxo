from rest_framework import serializers
from ..models import Colony, Oxxo


class ColonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Colony
        fields = [
            'id',
            'name',
        ]


class OxxoSerializer(serializers.ModelSerializer):
    colony = ColonySerializer()
    
    class Meta:
        model = Oxxo
        fields = [
            'id',
            'name',
            'colony',
            'lat',
            'lng',
            'allday',
            'beer',
            'parking'
        ]