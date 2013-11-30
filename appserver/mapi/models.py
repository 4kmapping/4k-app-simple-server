from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User, Group

# Create your models here.

class Project(Group):
	'''
	A place of collaboration to facilitate memebership info and project information 
	and security constrains.
	'''
	# sucurity level values: public | registered_users | project_only
	security_level = models.CharField(max_length=50, null=True, blank=True)
	desc = models.CharField(max_length=500, null=True, blank=True)


class Location(models.Model):
	# Location Data Fields (Same with mobile app)
	# ---
	# location id will be username + device_id + random hash string
	desc = models.TextField()
	tags = models.TextField() # comma separated list of tags.
	latitude = models.FloatField()
	longitude = models.FloatField()
	created = models.TimeField(null=True, blank=True) # data creation timestamp
	photoId = models.TextField(null=True, blank=True)

	evanType = models.BooleanField()
	trainType = models.BooleanField()
	mercyType = models.BooleanField()
	artsType = models.BooleanField()
	bibleStudyType = models.BooleanField()
	campusType = models.BooleanField()
	churchPlantingType = models.BooleanField()
	communityDevType = models.BooleanField()
	constructionType = models.BooleanField()
	counselingType  = models.BooleanField()
	healthcareType = models.BooleanField()
	hospitalType = models.BooleanField()
	indigenousType = models.BooleanField()
	mediaType = models.BooleanField()
	orphansType = models.BooleanField()
	prisonType = models.BooleanField()
	prostitutesType = models.BooleanField()
	researchType = models.BooleanField()
	urbanType = models.BooleanField()
	womenType = models.BooleanField()
	youthType = models.BooleanField()

	contactConfirmed = models.BooleanField()
	contactEmail = models.TextField(null=True, blank=True)
	contactPhone = models.TextField(null=True, blank=True)
	contactWebsite = models.TextField(null=True, blank=True)

	# Server side Information
	# These are additional data fields.
	# ---
	user = models.ForeignKey(User)
	# Group id is associate with any operation that takes more than one person's activities.
	project = models.ForeignKey(Project, null=True, blank=True)
	uploaded = models.TimeField(auto_now=True) # time at which data is uploaded
	# This oz_wid will contain an omega zone id and server side process will identify 
	# and store the zone id by looking at lat/lon in a record. 
	oz_wid = models.CharField(max_length=50, null=True, blank=True)


class LocationPicture(models.Model):
	'''
	Stores pictures taken on a location.
	'''
	pic = models.FileField(upload_to='Loc_Pics')
	# this from location orig_id
	username = models.TextField()


class LocationPictureForm(ModelForm):
	class Meta:
		model = LocationPicture
		fields = ['pic', 'username']











