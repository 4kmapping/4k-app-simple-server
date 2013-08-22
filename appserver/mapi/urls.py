from django.conf.urls import patterns, include, url


urlpatterns = patterns('mapi.views',
    url(r'^apikey', 'get_apikey'),
    
)