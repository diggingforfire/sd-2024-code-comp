from django.db import models
from django.utils import timezone

class Pet(models.Model):
    name = models.CharField(max_length=100)
    health = models.IntegerField(default=100)
    hunger = models.IntegerField(default=0)
    happiness = models.IntegerField(default=100)
    last_fed = models.DateTimeField(default=timezone.now)
    last_played = models.DateTimeField(default=timezone.now)

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.last_fed = timezone.now()

        self.decay_health()
        self.regen_health()

        self.save()

    def increase_hunger(self):
        time_since_fed = (timezone.now() - self.last_fed).total_seconds() / 60
        self.hunger = min(100, self.hunger + round(time_since_fed) * 5)

        self.decay_health()
        self.regen_health()

        self.save()

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.last_played = timezone.now()

        self.decay_health()
        self.regen_health()

        self.save()

    def decrease_happiness(self):
        time_since_played = (timezone.now() - self.last_played).total_seconds() / 60
        self.happiness = max(0, self.happiness - round(time_since_played) * 5)

        self.decay_health()
        self.regen_health()

        self.save()

    def decay_health(self):
        if self.hunger > 50:
            self.health = max(0, self.health - (self.hunger - 50) // 10)

        if self.happiness < 50:
            self.health = max(0, self.health - (50 - self.happiness) // 5)

    def regen_health(self):
        if self.hunger < 30 and self.happiness > 70:
            self.health = min(100, self.health + 5)
