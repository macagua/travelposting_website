from paypalrestsdk import util
from paypalrestsdk import resource

from apps.payments.paypal.api import default_api

DATE_FORMAT_PAYPAL = '%Y-%m-%dT%H:%M:%SZ'


class Resource(resource.Resource):
    def __init__(self, attributes=None, api=default_api):
        super(Resource, self).__init__(attributes, api)


class List(Resource, resource.List):
    @classmethod
    def all(cls, params=None, api=default_api):
        return super(List, cls).all(params, api)


class Find(Resource, resource.Find):
    @classmethod
    def find(cls, resource_id, api=default_api, refresh_token=None):
        return super(Find, cls).find(resource_id, api, refresh_token)


class Execute(resource.Post):
    def __init_subclass__(cls, **kwargs):
        pass


class ResourceMeta(type):
    def __new__(mcs, name, bases, attrs):
        extras = attrs.pop('extras')


class Active(resource.Post):
    def active(self, reason=None, refresh_token=None):
        url = util.join_url(self.path, str(self['id']), 'activate')
        data = {'reason': reason} if reason else {}
        _ = self.api.post(url, data, self.http_headers(), refresh_token)
        self.merge({'status': 'INACTIVE'})
        return self.success()


class Deactivate(resource.Post):
    def deactivate(self, refresh_token=None):
        url = util.join_url(self.path, str(self['id']), 'deactivate')
        _ = self.api.post(url, {}, self.http_headers(), refresh_token)
        self.merge({'status': 'ACTIVE'})
        return self.success()


class Cancel(resource.Post):
    def cancel(self, reason, refresh_token=None):
        url = util.join_url(self.path, str(self['id']), 'cancel')
        data = {'reason': reason}
        _ = self.api.post(url, data, self.http_headers(), refresh_token)
        self.merge({'status': 'CANCELLED'})
        return self.success()


class Capture(resource.Post):
    def capture(self, attributes=None, refresh_token=None):
        return self.post('capture', attributes, refresh_token)


class UpdatePrice(resource.Post):
    def update_price(self, attributes=None, refresh_token=None):
        """
        Actualiza el precio del plan especificado por el id
        :param attributes:
        :param refresh_token:
        :return: dict

        attributes = {
          "pricing_schemes": [
            {
              "billing_cycle_sequence": 2,
              "pricing_scheme": {
                "fixed_price": {
                  "value": "50",
                  "currency_code": "USD"
                }
              }
            }
          ]
        }
        """
        attributes = attributes or {}
        url = util.join_url(self.path, str(self['id']), 'activate')
        _ = self.api.post(url, attributes, self.http_headers(), refresh_token)
        return self.success()


class Suspend(resource.Post):
    def suspend(self, reason, refresh_token=None):
        url = util.join_url(self.path, str(self['id']), 'suspend')
        data = {'reason': reason}
        _ = self.api.post(url, data, self.http_headers(), refresh_token)
        self.merge({'status': 'SUSPENDED'})
        return self.success()


class Plan(List, resource.Create, Find, resource.Replace, Active, Deactivate, UpdatePrice):
    """Api new de plans
    """

    path = 'v1/billing/plans'

    # def update_price(self, attributes=None, refresh_token=None):
    #
    #     attributes = attributes or self.to_dict()
    #     url = util.join_url(self.path, str(self['id']), 'update-pricing-schemes')
    #     _ = self.api.post(url, attributes, self.http_headers(), refresh_token)
    #     self.error = None
    #     return self.success()


Plan.convert_resources['plan'] = Plan
Plan.convert_resources['plans'] = Plan


class Subscription(resource.Create, resource.Update, Find, resource.Replace, Active, Cancel, Capture, Suspend):
    """Api new of subscriptions"""

    path = 'v1/billing/subscriptions'

    def transactions(self, start_time, end_time, api=default_api):
        endpoint = util.join_url(self.path, str(self['id']), 'transactions')
        date_range = [('start_time', start_time.strftime(DATE_FORMAT_PAYPAL)),
                      ('end_time', end_time.strftime(DATE_FORMAT_PAYPAL))]
        url = util.join_url_params(endpoint, date_range)

        return Resource(self.api.get(url), api=api)

    @property
    def is_active(self):
        return self.status in ('ACTIVE', 'APPROVED', 'APPROVAL_PENDING')


Subscription.convert_resources['subscription'] = Subscription
Subscription.convert_resources['subscriptions'] = Subscription
