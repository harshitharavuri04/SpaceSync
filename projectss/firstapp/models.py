# models.py
from django.db import models


class Workspace(models.Model):
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    workspace_type = models.CharField(max_length=50)
    days_available = models.CharField(max_length=50)
    time_start = models.TimeField()
    end_start = models.TimeField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()

    class Meta:
        db_table = "Workspace"
