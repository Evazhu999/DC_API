# -*- coding: utf-8 -*-
'''
@Time    : 2020/4/7 14:22
@Author  : amay
@File    : test_fore.py
'''
import requests
from Config.conf import  *
#headers = {'user-agent': 'my-app/0.0.1'}
data={"mobile":"917838381868","phone_code":91}
data1={
	"mobile":"917838381868",
	"code":"123456",
	"phone_code":"91"
}
url_sms= requests.post(server_ip()+'/api/auth/sms',data=data)
url_login= requests.post(server_ip()+'/api/login',data=data1)

print(url_sms.text)
print(url_sms.status_code)
print(url_login.text)