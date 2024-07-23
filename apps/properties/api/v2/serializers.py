from rest_framework import serializers

from apps.pages.models import Banner
from apps.properties.models import PropertyType
from apps.pages.api.v1.serializers import WelcomeBaseSerializer


class PropertyMainSerializer(serializers.ModelSerializer):
    class Meta(WelcomeBaseSerializer.Meta):
        model = PropertyType
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
