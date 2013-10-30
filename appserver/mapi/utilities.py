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

        cnt = 0
        for tag in data['tags']:
            data['tags'][cnt] = escape(tag)
            cnt += 1

        return data