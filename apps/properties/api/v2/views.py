from rest_framework.response import Response
from rest_framework.views import APIView

from apps.pages.models import Banner
from apps.properties.api.v2.serializers import PropertyMainSerializer, BannerSerializer
from apps.properties.models import PropertyType


class PropertyMainView(APIView):
    def get(self, request, *args, **kwargs):
        data = {}

        property_types = PropertyType.objects.all()
        banners = Banner.objects.filter(page_for__in=['properties', 'all']).order_by('-is_active', '-created_at')
        data['property_types'] = PropertyMainSerializer(property_types, many=True, context={'request': request}).data
        data['banners'] = BannerSerializer(banners, many=True, context={'request': request}).data

        return Response(data)
