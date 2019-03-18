from rest_framework.viewsets import ModelViewSet
from ..models import Colony, Oxxo
from .serializers import ColonySerializer, OxxoSerializer


class ColonyViewSet(ModelViewSet):
    queryset = Colony.objects.all()
    serializer_class = ColonySerializer


class OxxoViewSet(ModelViewSet):
    queryset = Oxxo.objects.all()
    serializer_class = OxxoSerializer
