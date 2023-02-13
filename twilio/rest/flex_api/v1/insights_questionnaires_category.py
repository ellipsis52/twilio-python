"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Flex
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


class InsightsQuestionnairesCategoryContext(InstanceContext):
    def __init__(self, version: Version, category_id: str):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = { 'category_id': category_id,  }
        self._uri = '/Insights/QM/Categories/${category_id}'
        
    
    def delete(self, token):
        
        

        """
        Deletes the InsightsQuestionnairesCategoryInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri, )
    
    def update(self, token, body):
        data = values.of({
            'token': token,'body': body,
        })

        payload = self._version.update(method='post', uri=self._uri, data=data, )

        return InsightsQuestionnairesCategoryInstance(self._version, payload, category_id=self._solution['category_id'], )
        
        

        
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.InsightsQuestionnairesCategoryContext>'



class InsightsQuestionnairesCategoryInstance(InstanceResource):
    def __init__(self, version, payload, category_id: str):
        super().__init__(version)
        self._properties = { 
            'account_sid' : payload.get('account_sid'),
            'category_id' : payload.get('category_id'),
            'name' : payload.get('name'),
            'url' : payload.get('url'),
        }

        self._context = None
        self._solution = {
            'category_id': category_id or self._properties['category_id'],
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = InsightsQuestionnairesCategoryContext(
                self._version,
                category_id=self._solution['category_id'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.InsightsQuestionnairesCategoryInstance {}>'.format(context)



class InsightsQuestionnairesCategoryListInstance(ListResource):
    def __init__(self, version: Version):
        # TODO: needs autogenerated docs
        super().__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Insights/QM/Categories'
        
    
    """
    def create(self, token, body):
        data = values.of({
            'token': token,'body': body,
        })

        payload = self._version.create(method='post', uri=self._uri, data=data, )

        return InsightsQuestionnairesCategoryInstance(self._version, payload, )
        
    """
    
    """
    def page(self, token, page_size):
        
        data = values.of({
            'token': token,'page_size': page_size,
        })

        payload = self._version.create(method='get', uri=self._uri, data=data, )

        return InsightsQuestionnairesCategoryPage(self._version, payload, )
    """
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.InsightsQuestionnairesCategoryListInstance>'
