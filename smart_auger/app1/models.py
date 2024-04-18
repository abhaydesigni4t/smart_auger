from django.db import models


class data_management_model(models.Model):
    rec_no = models.AutoField(primary_key=True, unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

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

class Location(models.Model):
    rec_no = models.AutoField(primary_key=True,unique=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return str(self.rec_no)