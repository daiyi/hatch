from django.db import models


class Incubator(models.Model):
    owner = models.OneToOneField('account.Account')

    def __unicode__(self):
        return ("Incubator owned by account: " + self.owner.user.username)

class Egg(models.Model):
    # steps needed to hatch
    steps_needed = models.IntegerField(default=2000)
    # how many steps are recorded to this egg
    steps_received = models.IntegerField(default=0)
    # which incubator this egg belongs to
    incubator = models.ForeignKey('Incubator', null=True)

    def __unicode__(self):
        return ("Egg owned by account: " + self.incubator.owner.user.username)

