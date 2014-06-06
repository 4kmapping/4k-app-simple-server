from django.conf.urls import patterns, include, url


urlpatterns = patterns('main.views',
    url(r'^map', 'map'),
    url(r'^$', 'home'),
)






