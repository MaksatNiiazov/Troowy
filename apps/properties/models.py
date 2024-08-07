from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import CoreModel

User = get_user_model()


class Address(CoreModel):
    line1 = models.CharField(max_length=255, verbose_name=_("Адресная строка 1"),
                             help_text=_("Адрес, почтовый ящик, название компании"), )
    line2 = models.CharField(max_length=255, verbose_name=_("Адресная строка 2"), blank=True, null=True,
                             help_text=_("Квартира, офис, подразделение, здание, этаж и т.д."), )
    city = models.CharField(max_length=100, verbose_name=_("Город"))
    state_province = models.CharField(
        max_length=100, verbose_name=_("Штат/Провинция"), blank=True, null=True
    )
    postal_code = models.CharField(max_length=20, verbose_name=_("Почтовый индекс"))
    country = models.CharField(max_length=100, verbose_name=_("Страна"))
    longitude = models.FloatField(verbose_name=_("Долгота"), blank=True, null=True)
    latitude = models.FloatField(verbose_name=_("Широта"), blank=True, null=True)

    class Meta:
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")

    def __str__(self):
        return f'{self.country} {self.city} {self.line1} {self.line2}'


class Amenity(CoreModel):
    icon = models.FileField(
        upload_to="amenity_icons", blank=True, null=True, verbose_name=_("Иконка")
    )
    name = models.CharField(max_length=100, verbose_name=_("Название"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))

    class Meta:
        verbose_name = _("Удобство")
        verbose_name_plural = _("Удобства")


class PropertyType(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    icon = models.FileField(upload_to='images/categories/icons/', verbose_name=_("Иконка"), null=True, blank=True)

    class Meta:
        verbose_name = _("Тип недвижимости")
        verbose_name_plural = _("Типы недвижимости")
    def __str__(self):
        return self.name


class Property(CoreModel):
    property_type = models.ForeignKey(PropertyType, related_name='properties', on_delete=models.SET_NULL, null=True,
                                      verbose_name=_("Тип недвидимости"))
    address = models.ForeignKey(Address, on_delete=models.CASCADE, verbose_name=_("Адрес"))
    description = models.TextField(blank=True, verbose_name=_("Описание"))
    amenities = models.ManyToManyField(Amenity, blank=True, verbose_name=_("Удобства"))
    available = models.BooleanField(default=True, verbose_name=_("Доступно"))
    star_rating = models.IntegerField(verbose_name=_("Рейтинг звёзд"))
    name = models.CharField(max_length=100, verbose_name=_("Название"))
    rooms = models.IntegerField(help_text=_("Количество комнат"), verbose_name=_("Комнаты"))
    verified = models.BooleanField(default=False, verbose_name=_("Проверено"))

    class Meta:
        verbose_name = _("Недвижимость")
        verbose_name_plural = _("Недвижимость")


class PropertyPhoto(CoreModel):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name=_("Недвижимость"))
    photo = models.ImageField(upload_to="property_photos", verbose_name=_("Фото"))

    class Meta:
        verbose_name = _("Фотография недвижимости")
        verbose_name_plural = _("Фотографии недвижимости")


class RoomAmenity(CoreModel):
    icon = models.FileField(
        upload_to="amenity_icons", blank=True, null=True, verbose_name=_("Иконка")
    )
    name = models.CharField(max_length=100, verbose_name=_("Название"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))

    class Meta:
        verbose_name = _("Удобство комнаты")
        verbose_name_plural = _("Удобства комнат")

    def __str__(self):
        return self.name


class Room(CoreModel):
    hotel = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="hotel_rooms", verbose_name=_("Отель"))
    room_number = models.CharField(max_length=20, verbose_name=_("Номер комнаты"))
    room_type = models.CharField(max_length=20, verbose_name=_("Тип комнаты"))
    default_price_per_night = models.DecimalField(max_digits=10, decimal_places=2,
                                                  verbose_name=_("Стандартная цена за ночь"))
    amenities = models.ManyToManyField(RoomAmenity, blank=True, verbose_name=_("Удобства"))
    available = models.BooleanField(default=True, verbose_name=_("Доступна"))
    max_adults = models.IntegerField(verbose_name=_("Максимум взрослых"))
    max_children = models.IntegerField(verbose_name=_("Максимум детей"))
    max_animals = models.IntegerField(verbose_name=_("Максимум животных"))

    class Meta:
        verbose_name = _("Комната")
        verbose_name_plural = _("Комнаты")

    def __str__(self):
        return f'Комната №{self.room_number} / {self.room_type}'


class RoomPhotos(CoreModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name=_("Комната"))
    photo = models.ImageField(upload_to="room_photos", verbose_name=_("Фото"))

    class Meta:
        verbose_name = _("Фотография комнаты")
        verbose_name_plural = _("Фотографии комнаты")


class RoomPrice(CoreModel):
    rooms = models.ManyToManyField(Room, related_name='special_prices', verbose_name=_("Комнаты"))
    date_start = models.DateField(blank=True, verbose_name=_("Дата начала"))
    date_end = models.DateField(blank=True, verbose_name=_("Дата окончания"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена за ночь"))

    class Meta:
        verbose_name = _('Цена')
        verbose_name_plural = _('Цены')


class Review(models.Model):
    property = models.ForeignKey("Property", on_delete=models.CASCADE, related_name="reviews",
                                 verbose_name=_("Недвижимость"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", verbose_name=_("Пользователь"))
    comment = models.TextField(blank=True, null=True, help_text="Comment about the property", verbose_name=_("Коммент"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата создания"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Дата обновления"))

    class Meta:
        verbose_name = _("Отзыв")
        verbose_name_plural = _("Отзывы")

    def __str__(self):
        return f"Review by {self.user} for {self.property.name}"


class PaidService(CoreModel):
    name = models.CharField(max_length=100, verbose_name=_("Название"))
    description = models.TextField(blank=True, null=True, verbose_name=_("Описание"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Цена"))
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Зарплата"))

    class Meta:
        verbose_name = _("Платная услуга")
        verbose_name_plural = _("Платные услуги")

    def __str__(self):
        return self.name


class PropertyPaidService(CoreModel):
    """Through model for Property and PaidService many-to-many relationship."""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name=_("Недвижимость"))
    service = models.ForeignKey(PaidService, on_delete=models.CASCADE, verbose_name=_("Услуга"))

    class Meta:
        verbose_name = _("Платная услуга недвижимости")
        verbose_name_plural = _("Платные услуги недвижимости")

    def __str__(self):
        return f"{self.property.name} - {self.service.name}"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, related_name='bookings')
    guest_name = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Booking for {self.room.room_number} from {self.start_date} to {self.end_date}'
