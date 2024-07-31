import nested_admin
from django.contrib import admin

from .models import (
    Address,
    Amenity,
    Property,
    PropertyPhoto,
    Room,
    RoomAmenity,
    RoomPhotos,
    RoomPrice, PaidService, PropertyPaidService, PropertyType
)


class PropertyPhotoInline(nested_admin.NestedStackedInline):
    model = PropertyPhoto
    extra = 0
    fields = ["photo"]


class RoomPhotosInline(nested_admin.NestedStackedInline):
    model = RoomPhotos
    extra = 0
    fields = ["photo"]


class RoomInline(nested_admin.NestedStackedInline):
    model = Room
    inlines = [RoomPhotosInline]
    extra = 0
    fields = ["room_number", "room_type", "default_price_per_night", "available", 'max_adults', 'max_children',
              'amenities']


class PropertyPaidServiceInline(nested_admin.NestedStackedInline):
    model = PropertyPaidService
    extra = 0


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Property)
class PropertyAdmin(nested_admin.NestedModelAdmin):
    list_display = [
        "name",
        "property_type",
        "address",
        "available",
        "star_rating",
        "rooms",
        "verified",
    ]
    search_fields = [
        "name",
        "description",
    ]
    list_filter = [
        "available",
        "property_type",
        "verified",
    ]
    inlines = [PropertyPhotoInline, RoomInline, PropertyPaidServiceInline]
    filter_horizontal = ["amenities"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "description",
                    "property_type",
                    "star_rating",
                    "rooms",
                    "verified",
                    "available",
                )
            },
        ),
        ("Address", {"fields": ("address",)}),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "line1",
        "line2",
        "city",
        "state_province",
        "postal_code",
        "country",
    ]
    search_fields = ["line1", "city", "postal_code", "country"]
    list_filter = ["country", "state_province"]


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(RoomAmenity)
class RoomAmenityAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name"]


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(RoomPrice)
class PriceAdmin(admin.ModelAdmin):
    pass


@admin.register(PaidService)
class PaidServiceAdmin(admin.ModelAdmin):
    pass
