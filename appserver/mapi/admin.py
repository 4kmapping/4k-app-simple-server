from django.contrib import admin
from tastypie.admin import ApiKeyInline
from tastypie.models import ApiAccess, ApiKey
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from mapi.models import Location


class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]

admin.site.unregister(User)
admin.site.register(User,UserModelAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)