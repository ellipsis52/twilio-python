"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Video
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.base.page import Page

# 


class PublishedTrackContext(InstanceContext):
    def __init__(self, version: Version, room_sid: str, participant_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'participant_sid': participant_sid, 'sid': sid,  }
        self._uri = '/Rooms/${room_sid}/Participants/${participant_sid}/PublishedTracks/${sid}'
        
    
    def fetch(self):
        
        """
        Fetch the PublishedTrackInstance

        :returns: The fetched PublishedTrackInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return PublishedTrackInstance(self._version, payload, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'], sid=self._solution['sid'], )
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.PublishedTrackContext>'



class PublishedTrackInstance(InstanceResource):
    def __init__(self, version, payload, room_sid: str, participant_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'sid' : payload.get('sid'),
            'participant_sid' : payload.get('participant_sid'),
            'room_sid' : payload.get('room_sid'),
            'name' : payload.get('name'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'enabled' : payload.get('enabled'),
            'kind' : payload.get('kind'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'room_sid': room_sid or self._properties['room_sid'],'participant_sid': participant_sid or self._properties['participant_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = PublishedTrackContext(
                self._version,
                room_sid=self._solution['room_sid'],participant_sid=self._solution['participant_sid'],sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.PublishedTrackInstance {}>'.format(context)



class PublishedTrackListInstance(ListResource):
    def __init__(self, version: Version, room_sid: str, participant_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'room_sid': room_sid, 'participant_sid': participant_sid,  }
        self._uri = '/Rooms/${room_sid}/Participants/${participant_sid}/PublishedTracks'
        
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return PublishedTrackPage(self._version, payload, room_sid=self._solution['room_sid'], participant_sid=self._solution['participant_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.PublishedTrackListInstance>'
