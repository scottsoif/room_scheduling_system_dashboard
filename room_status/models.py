from django.db import models

# Create your models here.

class Rooms(models.Model):
    # room identifier
    room_name = models.CharField(max_length=20, primary_key=True)
    is_open = models.BooleanField()  # current status of the room
