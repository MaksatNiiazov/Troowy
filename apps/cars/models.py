from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BodyType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Car(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    body_type = models.ForeignKey(BodyType, on_delete=models.SET_NULL, null=True, related_name='cars')
    registration_number = models.CharField(max_length=20, unique=True)
    is_available = models.BooleanField(default=True)
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2)
    seats = models.IntegerField(default=4)
    transmission = models.CharField(max_length=50, choices=[('automatic', 'Automatic'), ('manual', 'Manual')])
    color = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) - {self.registration_number}"