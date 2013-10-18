from django.conf.urls import patterns, include, url


urlpatterns = patterns('mapi.views',
    url(r'^apikey', 'get_apikey'),
    url(r'^locpic', 'store_locpic'),
    url(r'^$', 'home')
)