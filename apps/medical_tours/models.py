from django.db import models
from django.utils import timezone


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    specialties = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.location})"


class MedicalTour(models.Model):
    name = models.CharField(max_length=100)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='medical_tours')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    includes = models.TextField()
    max_participants = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} at {self.clinic.name} from {self.start_date} to {self.end_date}"


class MedicalTourBooking(models.Model):
    medical_tour = models.ForeignKey(MedicalTour, on_delete=models.PROTECT, related_name='bookings')
    patient_name = models.CharField(max_length=100)
    patient_email = models.EmailField()
    number_of_participants = models.IntegerField()
    special_requirements = models.TextField(blank=True)
    booked_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.medical_tour.name} by {self.patient_name} on {self.booked_on.strftime('%Y-%m-%d')}"
