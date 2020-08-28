from rest_framework import viewsets
from .models import ClinicModel
from .serializers import ClinicSerializer


class ClinicViewset(viewsets.ModelViewSet):
    queryset = ClinicModel.objects.all()
    serializer_class = ClinicSerializer
