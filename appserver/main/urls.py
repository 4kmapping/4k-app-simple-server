from django.conf.urls import patterns, include, url


urlpatterns = patterns('main.views',
    url(r'^map', 'map'),
    url(r'^download', 'app_download'),                   
    url(r'^$', 'home'),
)




