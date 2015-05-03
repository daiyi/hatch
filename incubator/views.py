import json
from account.models import Account
from django.conf import settings
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from incubator.models import Egg, Incubator

from social.apps.django_app.utils import psa
from social.backends.oauth import BaseOAuth2
from social.backends.utils import load_backends

from incubator.decorators import render_to

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
    return render_to_response ('incubator.html',
                               context,
                               context_instance=RequestContext(request))

def context(**extra):
    return dict({
        'plus_id': getattr(settings, 'SOCIAL_AUTH_GOOGLE_PLUS_KEY', None),
        'plus_scope': ' '.join(GooglePlusAuth.DEFAULT_SCOPE),
        'available_backends': load_backends(settings.AUTHENTICATION_BACKENDS)
    }, **extra)

@render_to('home.html')
def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return redirect('done')
    return context()

@login_required
@render_to('home.html')
def done(request):
    """Login complete view, displays user data"""
    return context()

@psa('social:complete')
def ajax_auth(request, backend):
    if isinstance(request.backend, BaseOAuth2):
        token = request.REQUEST.get('access_token')
    else:
        raise HttpResponseBadRequest('Wrong backend type')
    user = request.backend.do_auth(token, ajax=True)
    login(request, user)
    data = {'id': user.id, 'username': user.username}
    return HttpResponse(json.dumps(data), mimetype='application/json')
