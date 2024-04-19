from django.db import models


class data_management_model(models.Model):
    rec_no = models.AutoField(primary_key=True, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()


    def __str__(self):
        return f"Recording {self.rec_no}"

    def as_dict(self):
        return {
            'lat': self.latitude,
            'lng': self.longitude,
            'name': f"Recording {self.rec_no}"
        }

    
class user_management_model(models.Model):
    sr = models.AutoField(primary_key=True,unique=True)
    username = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.username

from django.utils import timezone

from django.db import models
from django.utils import timezone

class Location(models.Model):
    rec_no = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.pk:  # Check if it's a new record
            # Get the maximum rec_no from existing records
            max_rec_no = Location.objects.aggregate(models.Max('rec_no'))['rec_no__max'] or 0
            # Set the new rec_no as the maximum rec_no + 1
            self.rec_no = max_rec_no + 1
        super(Location, self).save(*args, **kwargs)
