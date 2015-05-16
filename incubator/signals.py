from account.signals import user_signed_up
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
