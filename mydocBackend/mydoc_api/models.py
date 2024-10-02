from django.db import models
from django.contrib.auth.models import User

# Doctor model
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    specialization = models.CharField(max_length=100)
    image_url = models.URLField(null=True, blank=True)  # To store doctor's profile image
    rating = models.FloatField(default=0.0)
    fee = models.DecimalField(max_digits=6, decimal_places=2)  # Fee for consultation

    def __str__(self):
        return self.name

# Appointment model
class Appointment(models.Model):
    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('upcoming', 'Upcoming'),
        ('cancelled', 'Cancelled'),
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')

    def __str__(self):
        return f'{self.doctor.name} - {self.patient.username} - {self.appointment_date}'

# Available Time Slots for Doctors
class AvailableTimeSlot(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    available_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.doctor.name} - {self.available_date} - {self.start_time}'
