from django.db import models
import os
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.authentication.models import User
from apps.common.models import CoreModel


class Company(CoreModel):
    name = models.CharField(
        verbose_name=_("Название"), max_length=255, help_text=_("Имя Комании")
    )
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Владелец")
    )
    industry = models.CharField(
        verbose_name=_("Индустрия"), max_length=100, help_text=_("Промышленность")
    )
    address = models.CharField(
        verbose_name=_("Адрес"), max_length=500, help_text=_("Адрес компании")
    )
    phone = models.CharField(
        verbose_name=_("Номер телефона"), max_length=15, help_text=_("Телефонный номер")
    )
    email = models.EmailField(verbose_name=_("Почта"), help_text=_("Электронная почта"))
    website = models.URLField(verbose_name=_("Веб-сайт"), help_text=_("Сайт компании"))
    established_date = models.DateField(
        verbose_name=_("Дата основания"), help_text=_("Дата основания компании")
    )

    class Meta:
        verbose_name = _("Компания")
        verbose_name_plural = _("Компании")

    def __str__(self):
        return self.name


class CompanySector(CoreModel):
    class SectorName(models.TextChoices):
        HOTEL_BOOKINGS = "hotel_bookings", _("Бронирование отелей")
        CAR_RENTALS = "car_rentals", _("Аренда автомобилей")
        INTERNAL_TOURS = "internal_tours", _("Внутренние туры")
        INTERNATIONAL_TOURS = "international_tours", _("Международные туры")
        MEDICAL_TOURS = "medical_tours", _("Медицинские туры")
    sector = models.CharField(
        verbose_name=_("Название сектора"),
        max_length=50,
        choices=SectorName.choices,
        default=SectorName.HOTEL_BOOKINGS,
        help_text=_("Выберите сектор"),
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, verbose_name=_("Компания")
    )
    is_active = models.BooleanField(
        verbose_name=_("Активен"), default=True, help_text=_("Активный сектор")
    )
    verified = models.BooleanField(default=False, verbose_name=_("Проверен"))

    class Meta:
        verbose_name = _("Сектор компании")
        verbose_name_plural = _("Сектора компании")

    def __str__(self):
        return self.company.name + " - " + self.sector


def company_document_path(instance, filename):
    base, ext = os.path.splitext(filename)
    company_name = slugify(instance.company_sector.company.name)
    sector_name = slugify(instance.company_sector.sector.name)
    date_stamp = instance.upload_date.strftime("%Y-%m-%d")
    new_filename = f"{base}_{date_stamp}{ext}"
    return os.path.join("company_documents", company_name, sector_name, new_filename)


class Document(CoreModel):
    company_sector = models.ForeignKey(
        CompanySector, on_delete=models.CASCADE, verbose_name=_("Сектор компании")
    )
    verified = models.BooleanField(default=False)
    name = models.CharField(
        verbose_name=_("Имя документа"), max_length=255, help_text=_("Имя документа")
    )
    document = models.FileField(
        upload_to=company_document_path,
        blank=True,
        null=True,
        verbose_name=_("Документ"),
    )
    upload_date = models.DateTimeField(
        verbose_name=_("Дата загрузки"), help_text=_("Дата загрузки")
    )

    class Meta:
        verbose_name = _("Документ")
        verbose_name_plural = _("Документы")

    def __str__(self):
        return self.name
