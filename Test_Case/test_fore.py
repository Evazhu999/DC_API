# -*- coding: utf-8 -*-
'''
@Time    : 2020/4/7 14:22
@Author  : amay
@File    : test_fore.py
'''
import requests
#import time
from Config.conf import  *
#headers = {'user-agent': 'my-app/0.0.1'}
sms_data={"mobile":"917838381868","phone_code":91}
sms_url= requests.post(server_ip()+'/api/auth/sms',data=sms_data)
print('验证码发送成功接口返回：',sms_url.text)
#print(sms_url.status_code)
#time.sleep(3)
login_data={"mobile":"917838381868","code":"123456","phone_code":'91'}
login_url= requests.post(server_ip()+'/api/auth/login',data=login_data)
print('登录成功接口返回：',login_url.text)


