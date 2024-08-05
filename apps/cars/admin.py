from django.contrib import admin
from .models import City, Place, Car, Tariff, Service, ServiceType, Bid, Brand, BodyType, FuelType


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('title', 'archive')
    search_fields = ('title',)
    list_filter = ('archive',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'delivery_cost', 'archive')
    search_fields = ('title',)
    list_filter = ('city', 'archive')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'number', 'city', 'year', 'body_type', 'fuel_type', 'color', 'doors')
    search_fields = ('model', 'number')
    list_filter = ('brand', 'city', 'year', 'body_type', 'fuel_type', 'color')


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('car', 'deposit', 'min_days', 'max_days', 'cost_per_day')
    search_fields = ('car__model',)
    list_filter = ('car',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'service_type', 'archive')
    search_fields = ('title',)
    list_filter = ('service_type', 'archive')


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'car', 'begin', 'end', 'begin_place', 'end_place', 'prepayment')
    search_fields = ('fio', 'phone', 'car__model')
    list_filter = ('car', 'begin', 'end', 'begin_place', 'end_place')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
