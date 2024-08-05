from rest_framework import generics
from apps.cars.models import City, Place, Car, Tariff, Service, ServiceType, Bid
from .serializers import CitySerializer, PlaceSerializer, CarSerializer, TariffSerializer, ServiceSerializer, \
    ServiceTypeSerializer, BidSerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PlaceListView(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class TariffListView(generics.ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceTypeListView(generics.ListAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer


class BidListView(generics.ListCreateAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)