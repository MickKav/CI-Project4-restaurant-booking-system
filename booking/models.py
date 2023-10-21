from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_people = models.PositiveIntegerField()
    Date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name