"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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

# from twilio.rest.domain.auth_types import AuthTypesListInstancefrom twilio.rest.domain.credential_list_mapping import CredentialListMappingListInstancefrom twilio.rest.domain.ip_access_control_list_mapping import IpAccessControlListMappingListInstance


class DomainContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid, 'sid': sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains/${sid}.json'
        
        self._auth = None
        self._credential_list_mappings = None
        self._ip_access_control_list_mappings = None
    
    def delete(self):
        
        

        """
        Deletes the DomainInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def fetch(self):
        
        """
        Fetch the DomainInstance

        :returns: The fetched DomainInstance
        #TODO: add rtype docs
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return DomainInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        

        
    
    def update(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return DomainInstance(self._version, payload, account_sid=self._solution['account_sid'], sid=self._solution['sid'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DomainContext>'



class DomainInstance(InstanceResource):
    def __init__(self, version, payload, account_sid: str, sid: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'api_version' : payload.get('api_version'),
            'auth_type' : payload.get('auth_type'),
            'date_created' : payload.get('date_created'),
            'date_updated' : payload.get('date_updated'),
            'domain_name' : payload.get('domain_name'),
            'friendly_name' : payload.get('friendly_name'),
            'sid' : payload.get('sid'),
            'uri' : payload.get('uri'),
            'voice_fallback_method' : payload.get('voice_fallback_method'),
            'voice_fallback_url' : payload.get('voice_fallback_url'),
            'voice_method' : payload.get('voice_method'),
            'voice_status_callback_method' : payload.get('voice_status_callback_method'),
            'voice_status_callback_url' : payload.get('voice_status_callback_url'),
            'voice_url' : payload.get('voice_url'),
            'subresource_uris' : payload.get('subresource_uris'),
            'sip_registration' : payload.get('sip_registration'),
            'emergency_calling_enabled' : payload.get('emergency_calling_enabled'),
            'secure' : payload.get('secure'),
            'byoc_trunk_sid' : payload.get('byoc_trunk_sid'),
            'emergency_caller_sid' : payload.get('emergency_caller_sid'),
        }

        self._context = None
        self._solution = {
            'account_sid': account_sid or self._properties['account_sid'],'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = DomainContext(
                self._version,
                account_sid=self._solution['account_sid'],sid=self._solution['sid'],
            )
        return self._context

    @property
    def auth(self):
        return self._proxy.auth
    @property
    def credential_list_mappings(self):
        return self._proxy.credential_list_mappings
    @property
    def ip_access_control_list_mappings(self):
        return self._proxy.ip_access_control_list_mappings
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.DomainInstance {}>'.format(context)



class DomainListInstance(ListResource):
    def __init__(self, version: Version, account_sid: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'account_sid': account_sid,  }
        self._uri = '/Accounts/${account_sid}/SIP/Domains.json'
        
    
    """
    def create(self, body):
        data = values.of({
            'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return DomainInstance(self._version, payload, account_sid=self._solution['account_sid'])
        
    """
    
    """
    def page(self, page_size):
        
        data = values.of({
            'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return DomainPage(self._version, payload, account_sid=self._solution['account_sid'], )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.DomainListInstance>'
