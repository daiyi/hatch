from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from incubator.models import Egg, Incubator
from account.models import Account
def index(request):
    context = {
        'message': "Hello egg"
    }
    return render(request,'incubator.html', context)

def current_egg(request):
    """
    Shows the current egg.
    """
    context = {}

    if request.user.is_authenticated():
        current_user = request.user
        user = Account.objects.select_related('user').filter(user=current_user)
        incubator = Incubator.objects.select_related('owner').filter(owner=user)
        egg_query = Egg.objects.select_related('incubator').filter(incubator=incubator)
        context['egg'] = egg_query[0]
        context['steps'] = context['egg'].steps_received
        context['current_user'] = current_user

    else:
        # user not logged in
        context['message'] = "walk to hatch eggs"
    return render(request, 
                  'incubator.html',
                  context)
