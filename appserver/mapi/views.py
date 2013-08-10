from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from sys import stdout


def http_login(request):
	'''
	Provide a basic authentication for mobile app.
	'''
	
	if 'HTTP_AUTHORIZATION' in request.META:
		auth = request.META['HTTP_AUTHORIZATION'].split()
		# for debugging
		stdout(request.META)
		if len(auth) == 2:
			if auth[0].lower() == 'basic':
				uname, passwd = base64.b64decode(auth[1]).split(':')
				user = authenticate(username=uname, password=passwd)
				if user is not None and user.is_active:
					login(request.user)
					request.user = user
				else: # if authentication fails.
					response = HttpResponse()
					response.status_code = 403
					response['WWW-Authenticate'] = 'Basic realm="%$"' % realm
					return response
	
	response = HttpResponse()
	response.status_code = 401
	response['WWW-Authenticate'] = 'Basic realm="%$"' % realm
	return response
	
	
	


