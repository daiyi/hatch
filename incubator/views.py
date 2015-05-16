import json
from account.models import Account
from django.conf import settings
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from incubator.models import Egg, Incubator
import requests
from social.apps.django_app.default.models import UserSocialAuth
from social.apps.django_app.utils import psa
from social.backends.oauth import BaseOAuth2
from social.backends.utils import load_backends
import time
from incubator.decorators import render_to

def index(request):
    context = {
        'message': "Hello egg"
    }
    return render(request,'incubator.html', context)

def current_egg(request):
    """
    Shows the current focused egg.
    """
    params = {}

    # If user is logged in
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        incubator = Incubator.objects.select_related('owner').get(owner=user)
        egg = Egg.objects.select_related('incubator').filter(incubator=incubator, focus=True).get()        
        if UserSocialAuth.objects.filter(user=user).exists():
            # currently only google_fit authentication is supported
            google_fit_auth = UserSocialAuth.objects.filter(user=user).get()
            params['social'] = True

            check_time = int(time.time())
            url = 'https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:estimated_steps/datasets/' + \
                  str(incubator.last_updated) + '000000000' + '-' + \
                  str(check_time)+ '000000000'
            print "#######"
            print url
            
            response = requests.get(
                url,
                params={'access_token': google_fit_auth.extra_data['access_token']}
            )
            print response.json()
            if 'point' in response.json():
                steps = 0
                for point in response.json()['point']:
                    steps += point['value'][0]['intVal']
                params['new_steps'] = steps
                egg.steps_received += steps
                egg.save()
                incubator.last_updated = check_time
                incubator.save()
            elif 'error' in response.json():
                params['new_steps'] = -1
            else:
                params['new_steps'] = "No"
        

    # user not logged in
    else:
        params['message'] = "walk to hatch eggs"

    params['egg'] = egg
    return render_to_response ('incubator.html',
                               params,
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
