from account.signals import user_signed_up
from django.conf import settings
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from incubator.models import Incubator, Egg
from sys import stderr


@receiver(user_signed_up)
def new_account_handler(sender, **kwargs):
    if not 'user' in kwargs:
        sys.stderr.write("Newly created user not provided!")
        return
    user = kwargs['user']
    incubator = Incubator(owner=user)
    incubator.save()
        
    egg = Egg(incubator=incubator, focus=True)
    egg.save()

#@receiver(user_logged_in)
#def sig_user_logged_in(sender, user, request, **kwargs):
#    print "################## log in"
#    
#@receiver(user_logged_out)
#def sig_user_logged_out(sender, user, request, **kwargs):
#    print "################## log out"
