__author__ = 'andrius'

from django.utils.module_loading import import_string
from django.core.exceptions import ImproperlyConfigured

from django.conf import settings

class SmsTransportFactory(object):
    def __init__(self):
        self.sms_transports = {}
        if self.settings_valid():
            self.init_trasports()
        else:
            raise ImproperlyConfigured

    def __getitem__(self, name):
        return self.sms_transports[name]

    def settings_valid(self):
        try:
            tmp = settings.SMS_TRANSPORTS
            return True
        except:
            return False

    def init_trasports(self):
        for name, description in settings.SMS_TRANSPORTS.items():
            cls = import_string(description['BACKEND'])
            self.sms_transports[name] = cls(description.get('PARAMS', {}))


sms_transports = SmsTransportFactory()
sms_transport = sms_transports['default']

