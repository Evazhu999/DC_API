# -*- coding: utf-8 -*-
'''
@Time    : 2020/4/7 14:22
@Author  : amay
@File    : test_fore.py
'''
import requests
#import time
from Config.conf import  *
sms_data={"mobile":"917838381868","phone_code":91}
sms_url= requests.post(server_ip()+'/api/auth/sms',json=sms_data)
print('验证码已发送：',sms_url.text)
#print(sms_url.status_code)
#time.sleep(3)
login_data={"mobile":"917838381868","code":"123456","phone_code":'91'}
login_url= requests.post(server_ip()+'/api/auth/login',json=login_data)
print('登录成功：',login_url.text)
access_token=login_url
login_token=login_url.json().get(access_token)
print(login_token)

