from django.conf.urls import patterns, include, url
from tastypie.api import Api
from mapi.api import UserResource, LocationResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Resource registration
v01_api = Api(api_name='0.1')
v01_api.register(UserResource())
v01_api.register(LocationResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'appserver.views.home', name='home'),
    # url(r'^appserver/', include('appserver.foo.urls')),

	# url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v01_api.urls)),
    url(r'^m/', include('mapi.urls')),
    
)
