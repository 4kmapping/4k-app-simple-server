from django.utils import simplejson
from django.core.serializers import json
from tastypie.serializers import Serializer
from cgi import escape

class LocationJSONSerializer(Serializer):
    ''' To prevent XSS vulnerability, it will escape < > and so on for inserting records.'''    

    def from_json(self, content):

        data = simplejson.loads(content)
        # escape 'desc'
        data['desc'] = escape(data['desc'])
        data['tags'] = escape(data['tags'])

        return data