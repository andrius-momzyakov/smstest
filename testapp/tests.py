from django.test import TestCase

from libsms import sms_transports
from libsms import sms_transport

# Create your tests here.

class SmsTestCase(TestCase):
    def test_default_backend(self):
        sms_transport.send(phone='111', msg='test default')

    def test_dummy_backend(self):
        sms_transports['dummy'].send(phone='222', msg='test dummy')

    def test_other_backend(self):
        sms_transports['other'].send(phone='333', msg='test other')
