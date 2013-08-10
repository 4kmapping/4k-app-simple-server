from django.conf.urls import patterns, include, url


urlpatterns = patterns('mapi.views',
    url(r'^login', 'http_login'),
    
)