__author__ = 'andrius'

class BaseSmsTransport(object):
    def __init__(self, params):
        self.params = params

    def send(self, phone, msg):
        print('phone={0}'.format(phone))
        print('msg={0}'.format(msg))
