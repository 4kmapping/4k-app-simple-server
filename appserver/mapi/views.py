from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
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

	
	


