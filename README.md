# smstest

Тестовое задание по подготовке тестовой библиотеки для встраиваемых в проекты django sms-транспортов.

## Использование

from libsms import sms_transport

from libsms import sms_transports

sms_transport.send(phone=’123123’, msg=’qweqwe’) # транспорт по умолчанию
sms_transports[‘dummy’].send(phone=’123123’, msg=’qweqwe’)

## Деплой:

1. Скопировать папку libsms в папку проекта
2. В settings.py проекта или в dgango.conf.global_settings.py прописать 

SMS_TRANSPORTS = {
		'default': {
			'BACKEND' : 'libsms.backends.sms.SmsTransport',
			'PARAMS' : {
				'login' : 'some_login',
				'password' : 'some_password',
			}
		},
		'dummy': {
			'BACKEND' : 'libsms.backends.dummy.SmsTransport',
		},
		'other': {
			'BACKEND' : 'libsms.backends.other.SmsTransport',
			'PARAMS' : {
				'login' : 'some_login',
				'password' : 'some_password',
				'var1' : 'var1',
				'var2' : 'var2',
			}
		}
	}

## Тест

Скопировать папку проекта, войти в нее и выполнить 

python manage.py test


