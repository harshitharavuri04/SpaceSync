from django.contrib.auth.models import User
from django.db import models

class Workspace(models.Model):
    CITY_CHOICES = [
        ('Hyderabad', 'Hyderabad'),
        ('Banglore', 'Banglore'),
        # Add more city choices as needed
    ]

    WORKSPACE_TYPE_CHOICES = [
        ('coworking', 'Co-working Space'),
        ('conference', 'Conference Rooms'),
        ('virtual', 'Virtual Office'),
        ('cabins', 'Private Cabins'),
        ('meeting', 'Meeting Rooms'),
        ('personal', 'Personalized Desk'),
        # Add more workspace type choices as needed
    ]

    FURNITURE_CHOICES = [
        ('furnished', 'Furnished'),
        ('unfurnished', 'Unfurnished'),
        # Add more furniture choices as needed
    ]

    PARKING_CHOICES = [
        ('not-available', 'Not Available'),
        ('Available', 'Available'),
        # Add more parking choices as needed
    ]

    DURATION_CHOICES = [
        ('day', 'Days'),
        ('week', 'Weeks'),
        ('month', 'Months'),
        # Add more duration choices as needed
    ]

    CANCELLATION_POLICY_CHOICES = [
        ('flexible', 'Flexible'),
        ('strict', 'Strict'),
        # Add more cancellation policy choices as needed
    ]

    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    address = models.TextField()
    workspace_type = models.CharField(max_length=100, choices=WORKSPACE_TYPE_CHOICES)
    furniture = models.CharField(max_length=100, choices=FURNITURE_CHOICES)
    parking = models.CharField(max_length=100, choices=PARKING_CHOICES)
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    cancellation_policy = models.CharField(max_length=100, choices=CANCELLATION_POLICY_CHOICES)
    image_upload = models.ImageField(upload_to='workspace_images/')

    def __str__(self):
        return f"{self.workspace_type} in {self.city}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
