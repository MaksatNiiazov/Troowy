from django.db import models
from django.utils import timezone


class TourOperator(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    description = models.TextField()
    attractions = models.TextField()

    def __str__(self):
        return f"{self.name}, {self.country}"


class Tour(models.Model):
    name = models.CharField(max_length=100)
    operator = models.ForeignKey(TourOperator, on_delete=models.CASCADE, related_name='tours')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tours')
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_participants = models.IntegerField()
    details = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.destination.name}) from {self.start_date} to {self.end_date}"


class TourBooking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.PROTECT, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    number_of_participants = models.IntegerField()
    booked_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.tour.name} by {self.customer_name} on {self.booked_on.strftime('%Y-%m-%d')}"
