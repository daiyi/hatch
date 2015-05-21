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
import egg_utils as ut
import json
from incubator.models import Egg, Incubator
import os
import requests
from social.apps.django_app.default.models import UserSocialAuth
from social.apps.django_app.utils import psa
from social.backends.oauth import BaseOAuth2
from social.backends.utils import load_backends
import time
from incubator.decorators import render_to


def index(request):
    if request.user.is_authenticated():
        return incubator(request, request.user.username)
        
    return render_to_response ('splash.html', {},
                               context_instance=RequestContext(request))        


def incubator(request, username):
    """
    Shows the current focused egg.
    """
    params = {}
    
    user = ut.get_user(username)

    incubator = ut.get_incubator(user=user)
    egg = ut.get_egg(incubator=incubator)
    other_eggs = Egg.objects.select_related('incubator').filter(incubator=incubator, focus=False)

    # pokemon reactions
    #for egger in other_eggs:
    #    file = settings.STATIC_ROOT + '/pkmn/' + egger.identity + '-2.gif'
    #    if os.path.isfile(file):
    #        params[egger]['reaction_gif'] = file


    # Show user's page controls 
    if (request.user.is_authenticated() and username == request.user.username):

        params['authorized'] = True

        if UserSocialAuth.objects.filter(user=user).exists():
            # currently only google_fit authentication is supported
            google_fit_auth = UserSocialAuth.objects.filter(user=user).get()
            params['social'] = True

            check_time = int(time.time())
            url = 'https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.step_count.delta:com.google.android.gms:estimated_steps/datasets/' + \
                  str(incubator.last_updated) + '000000000' + '-' + \
                  str(check_time)+ '000000000'

            response = requests.get(
                url,
                params={'access_token': google_fit_auth.extra_data['access_token']}
            )

            if 'point' in response.json():
                steps = 0
                for point in response.json()['point']:
                    steps += point['value'][0]['intVal']
                    egg.new_steps = steps
                    egg.steps_received += steps
                    incubator.last_updated = check_time                
                    incubator.save()
                    egg.save()

            elif 'error' in response.json():
                egg.new_steps = -1
            else:
                egg.new_steps = 0

            if (egg.steps_received > egg.steps_needed) and (egg.next_identity != ''):
                ut.evolve(egg)

    params['other_eggs'] = other_eggs
    params['last_updated'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(incubator.last_updated))
    params['egg'] = ut.message(egg, username)
            
    return render_to_response ('incubator.html',
                               params,
                               context_instance=RequestContext(request))

def api(request, param):
    if param == 'newegg':
        incubator = ut.get_incubator(request.user)
        
        prev_egg = ut.get_egg(incubator=incubator)
        prev_egg.focus = False
        prev_egg.save()
        
        egg = Egg(incubator=incubator, focus=True)
        egg.save()
        
        response = {'egg':{'url':'https://convox.org/h/static/pkmn/egg.gif',
                           'message':'this is your new egg.'}}
    else:
        response = {'message':'omg'}

    return HttpResponse(json.dumps(response),
                        content_type="application/json")

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
