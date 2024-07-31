from django.db import models

class City(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название города")
    archive = models.BooleanField(default=False, verbose_name="Архив")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Бренд")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

class BodyType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип кузова")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип кузова"
        verbose_name_plural = "Типы кузова"

class FuelType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип топлива")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип топлива"
        verbose_name_plural = "Типы топлива"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Бренд")
    model = models.CharField(max_length=100, verbose_name="Марка и модель")
    number = models.CharField(max_length=20, verbose_name="Гос. номер")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    year = models.PositiveIntegerField(verbose_name="Год выпуска")
    body_type = models.ForeignKey(BodyType, on_delete=models.CASCADE, verbose_name="Тип кузова")
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, verbose_name="Тип топлива")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    doors = models.PositiveIntegerField(verbose_name="Количество дверей")
    photo_guid = models.CharField(max_length=36, verbose_name="GUID фотографии")

    def __str__(self):
        return f"{self.brand.name} {self.model} ({self.number})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

class Place(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название места")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Город")
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость доставки")
    archive = models.BooleanField(default=False, verbose_name="Архив")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место выдачи/возврата"
        verbose_name_plural = "Места выдачи/возврата"

class Tariff(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Залог")
    min_days = models.PositiveIntegerField(verbose_name="Минимальное количество дней")
    max_days = models.PositiveIntegerField(verbose_name="Максимальное количество дней")
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость аренды за день")

    def __str__(self):
        return f"Тариф для {self.car.brand.name} {self.car.model}"

    class Meta:
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

class ServiceType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название типа услуги")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тип услуги"
        verbose_name_plural = "Типы услуг"

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название услуги")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, verbose_name="Тип услуги")
    archive = models.BooleanField(default=False, verbose_name="Архив")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Bid(models.Model):
    NEW = 'new'
    ACCEPTED_AS_RESERVE = 'accepted_as_reserve'
    ACCEPTED_AS_RENT = 'accepted_as_rent'
    REJECTED = 'rejected'
    DELETED = 'deleted'

    STATUS_CHOICES = [
        (NEW, 'На рассмотрении'),
        (ACCEPTED_AS_RESERVE, 'Создана бронь'),
        (ACCEPTED_AS_RENT, 'Создана аренда'),
        (REJECTED, 'Заявка отклонена'),
        (DELETED, 'Заявка удалена'),
    ]

    fio = models.CharField(max_length=100, verbose_name="ФИО клиента")
    phone = models.CharField(max_length=15, verbose_name="Телефон клиента")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    begin = models.DateTimeField(verbose_name="Начало периода")
    end = models.DateTimeField(verbose_name="Окончание периода")
    begin_place = models.ForeignKey(Place, related_name='begin_place', on_delete=models.CASCADE, verbose_name="Место выдачи")
    end_place = models.ForeignKey(Place, related_name='end_place', on_delete=models.CASCADE, verbose_name="Место возврата")
    services = models.ManyToManyField(Service, blank=True, verbose_name="Услуги")
    prepayment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Предоплата")

    def __str__(self):
        return f"Заявка {self.fio} на {self.car.brand.name} {self.car.model}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-begin']

class Payment(models.Model):
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, verbose_name="Заявка")
    summ = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма оплаты")
    transaction_id = models.CharField(max_length=100, verbose_name="Идентификатор транзакции")

    def __str__(self):
        return f"Оплата {self.bid} на сумму {self.summ}"

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
