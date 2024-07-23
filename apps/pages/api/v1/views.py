from rest_framework.views import APIView

from apps.pages.api.v1.serializers import (
    StaticPageSerializer, WelcomePropertySerializer, WelcomeCarsSerializer, WelcomeToursSerializer,
    WelcomeInternationalToursSerializer, WelcomeMedicalToursSerializer
)
from rest_framework import generics
from rest_framework.response import Response

from apps.pages.models import (
    StaticPage, WelcomeProperty, WelcomeCars, WelcomeTours, WelcomeInternationalTours, WelcomeMedicalTours,
)


class StaticPageDetailView(generics.RetrieveAPIView):
    queryset = StaticPage.objects.all()
    serializer_class = StaticPageSerializer
    lookup_field = 'slug'

    def get_object(self):
        slug = self.kwargs['slug']
        instance = None

        try:
            instance = StaticPage.objects.get(slug=slug)
        except StaticPage.DoesNotExist:
            if slug == 'about-us':
                instance = StaticPage.objects.create(
                    title='',

                    content='',

                    slug="about-us"
                )

        return instance

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class WellcomePageView(APIView):
    def get(self, request, *args, **kwargs):
        data = {}

        properties = WelcomeProperty.objects.all()
        cars = WelcomeCars.objects.all()
        tours = WelcomeTours.objects.all()
        international_tours = WelcomeInternationalTours.objects.all()
        medical_tours = WelcomeMedicalTours.objects.all()

        data['properties'] = WelcomePropertySerializer(properties, many=True, context={'request': request}).data
        data['cars'] = WelcomeCarsSerializer(cars, many=True, context={'request': request}).data
        data['tours'] = WelcomeToursSerializer(tours, many=True, context={'request': request}).data
        data['international_tours'] = WelcomeInternationalToursSerializer(international_tours, many=True,
                                                                          context={'request': request}).data
        data['medical_tours'] = WelcomeMedicalToursSerializer(medical_tours, many=True,
                                                              context={'request': request}).data

        return Response(data)
