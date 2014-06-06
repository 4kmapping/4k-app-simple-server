from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.http import HttpResponseBadRequest, HttpResponseNotAllowed 
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from mapi.models import LocationPicture, LocationPictureForm
from sys import stdout
from tastypie.models import ApiKey
import base64

import logging

logger = logging.getLogger(__name__)

@csrf_exempt
def get_apikey(request):

	'''
	Provide an API key for a user after authenticating the user. 
    Once a user get the token, the token will be used for communication instead of password.
    '''

	if request.POST:

		if 'username' not in request.POST or 'password' not in request.POST:
			response = HttpResponse()
			response.status_code = 401
			return response

		username = request.POST.get('username','no_user')
        raw_passwd = request.POST.get('password','')
        password = base64.b64decode(raw_passwd)
        #logger.error(username, password)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
			# From DB, get a corresponding ApiKey for a user.
			apikey = ApiKey.objects.get(user=user)
			res_txt = 'apikey:%s' % apikey.key
			# Prepare response and send it.
			response = HttpResponse()
			response.status_code = 200
			response.write(res_txt)
			return response
        else:
			response = HttpResponse()
			response.status_code = 403
			return response

	response = HttpResponse()
	response.status_code = 401
	return response



@csrf_exempt	
def store_locpic(request):
    '''
    Store a loction picture from mobile application request.
    '''

    username = ''

    if request.method == 'POST':
        # Authenticate user with username & ApiKey in header
        # ---

        print "in side of photo POST"

        if (request.META.get('HTTP_AUTHORIZATION') and 
            request.META['HTTP_AUTHORIZATION'].lower().startswith('apikey')):
            (auth_type, data) = request.META['HTTP_AUTHORIZATION'].split()

            if auth_type.lower() != 'apikey':

                print 'apikey is not set', auth_type.lower()

                return HttpResponseBadRequest()

            username, api_key = data.split(':',1)
            # Grab user and his/her apikey from db.
            try:
                user = User.objects.get(username=username)
                key = ApiKey.objects.get(user=user)
                
                if key.key != api_key:

                    print 'key is different'

                    return HttpResponseForbidden()
            except ValueError:

                print 'Storing photo failed'

                return HttpResponseBadRequest()
        else:
            
            print 'photo POSTing, authorization failed'

            return HttpResponseBadRequest()

        # Request passed authentication, now store picture.
        # ---
        form = LocationPictureForm(request.POST, request.FILES)
        
        if form.is_valid():
            locpic = form.save(commit=False)
            locpic.username = username
            locpic.save()
            print 'picture %s from %s saved successfully' % (locpic.pic.name, 
                locpic.username)
            return HttpResponse('The picture was saved successfully.')
        else:
            response = HttpResponseBadRequest()
            response['REASON'] = 'Form is invalid.'

            print 'form is not vaild', form.errors

            return response   
        
    else:
        print "Error!"
        return HttpResponseNotAllowed('Allowed HTTP methods are: POST')

    print "Error at the bottom"
    return HttpResponseBadRequest('Reached the end without saving.')
