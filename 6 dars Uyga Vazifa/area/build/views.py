from django.shortcuts import render
from rest_framework import viewsets
from .models import Area, Organization, Construction
from .serializers import AreaSerializer, OrganizationSerializer, ConstructionSerializer
from rest_framework import permissions

# Create your views here.


class AreaAPIViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    permission_classes = (permissions.IsAdminUser,)


class ConstructionAPIViewSet(viewsets.ModelViewSet):
    queryset = Construction.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticated,)


class OrganizationAPIViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)




