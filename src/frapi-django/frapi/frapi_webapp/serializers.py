from rest_framework import serializers
from .models import Maire, Region


class MaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maire
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
