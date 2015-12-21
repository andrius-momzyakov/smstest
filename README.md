# smstest

## Установка

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

Скопировать прпку проекта, войти в нее и выполнить 

python manage.py test


