from django.db import models

class Egg(models.Model):
    steps_needed = models.IntegerField(default=2000)
    steps_received = models.IntegerField(default=0)
