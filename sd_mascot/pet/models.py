from django.db import models
from django.utils import timezone

class Pet(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=100)
    hunger = models.IntegerField(default=0)  # Hunger increases over time
    happiness = models.IntegerField(default=100) # Happiness decreases over time
    last_fed = models.DateTimeField(default=timezone.now)
    last_played = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name