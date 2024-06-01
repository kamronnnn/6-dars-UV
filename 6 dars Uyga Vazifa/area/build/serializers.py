from rest_framework import serializers
from .models import Area, Organization, Construction


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class ConstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construction
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


