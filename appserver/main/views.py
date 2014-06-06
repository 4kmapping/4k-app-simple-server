from django.shortcuts import render_to_response
from django.template import RequestContext
from mapi.models import Location
from django.core import serializers


def home(request):
    return render_to_response('main/home.html',{}, context_instance=RequestContext(request))
    
    
def map(request, prjid=None):
    if prjid:
        locations = Location(project=prjid).objects
    else:
        locations = Location.objects.all()
    
    locs_json = serializers.serialize('json', locations)
    return render_to_response('main/map.html',{'locations':locs_json}, 
        context_instance = RequestContext(request))