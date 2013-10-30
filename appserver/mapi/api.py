from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.models import ApiKey
from tastypie import fields
from tastypie.authentication import SessionAuthentication, BasicAuthentication, ApiKeyAuthentication
from mapi.models import Location, LocationPicture
from mapi.MAPIAuthorization import UserObjectsOnlyAuthorization
from django.contrib.auth.models import User
from utilities import LocationJSONSerializer



class LocationPictureResource(ModelResource):
    pic = fields.FileField(attribute='pic')
    class Meta:
        queryset = LocationPicture.objects.all()
        resource_name = 'loc_pic'
        authentication = ApiKeyAuthentication()



class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all() 
        resource_name = 'user'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        filtering = { 'username': ALL, 'id': ALL, }
        authentication=ApiKeyAuthentication() 



class LocationResource(ModelResource):
# To include user info
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Location.objects.all()
        list_allowed_methods = ['get', 'post']
        #detail_allowed_methods = ['get', 'post', 'put', 'delete']
        resource_name = 'location'
        excludes = ['user_group','uploaded','oz_wid']
        authentication = ApiKeyAuthentication()
        authorization = UserObjectsOnlyAuthorization()
        filtering = {
            'user': ALL_WITH_RELATIONS,
        }  
        serializer = LocationJSONSerializer()		

    '''
    Custom object creation to set user from request and authentication mechanism.
        (Another Example):
        def obj_create(self, bundle, **kwargs):
            return super(LocationResource, self).obj_create(bundle, user=bundle.request.user)

    '''
    def obj_create(self, bundle, **kwargs):
        kwargs['user'] = bundle.request.user       
        return super(LocationResource, self).obj_create(bundle, **kwargs)


