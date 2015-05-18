from django.db import models
import time


def epoch_time_now():
    return int(time.time())


class Incubator(models.Model):

    owner = models.OneToOneField('auth.User')

    # Epoch time in seconds of the last update to focused eggs in Incubator
    last_updated = models.PositiveIntegerField(default=epoch_time_now)
    
    def __unicode__(self):
        return (self.owner.username + "'s incubator")

class Egg(models.Model):
    # True if egg is receiving stimulus, False if egg is stored.
    focus = models.BooleanField(default=False)
    
    # steps needed to hatch
    steps_needed = models.IntegerField(default=2000)
    
    # how many steps are recorded to this egg
    steps_received = models.IntegerField(default=0)

    # the species of this egg
    identity = models.CharField(max_length=12, default='egg')

    # what the egg will evolve into
    next_identity = models.CharField(max_length=12, default='kanto', blank=True)

    # name to be assigned by user
    nickname = models.CharField(max_length=12, default='', blank=True)

    # time when egg was created
    time_created = models.DateTimeField(auto_now_add=True)
    
    # which incubator this egg belongs to
    incubator = models.ForeignKey('Incubator', null=True)

    def __unicode__(self):
        return (self.identity + " egg | owner: " + self.incubator.owner.username)
