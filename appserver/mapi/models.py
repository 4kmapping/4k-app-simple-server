from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Location(models.Model):
	orig_id = models.IntegerField(max_length=200)
	desc = models.TextField()
	tags = models.TextField() # comma separated list of tags.
	lat = models.FloatField()
	lon = models.FloatField()
	created = models.TimeField(null=True, blank=True) # data creation timestamp
	# Server side Information
	# ---
	user = models.ForeignKey(User)
	# Group id is associate with any operation that takes more than one person's activities.
	user_group = models.ForeignKey(Group, null=True, blank=True)
	uploaded = models.TimeField(auto_now=True) # time at which data is uploaded
	# This oz_wid will contain an omega zone id and server side process will identify 
	# and store the zone id by looking at lat/lon in a record. 
	oz_wid = models.CharField(max_length=50, null=True, blank=True)
	
	