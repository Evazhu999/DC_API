# -*- coding: utf-8 -*-
'''
@Time    : 2020/4/7 14:22
@Author  : amay
@File    : test_fore.py
'''
import requests
import time
from Config.conf import  *
import json
import random

#随机手机号
phone_end = ''.join(random.sample('1234567890',8))
phone_no = '9178' + phone_end
#商户后台--商户相关接口
# sms_data={"mobile":"917838381867","phone_code":91}#短信发送接口
sms_data={"mobile":phone_no,"phone_code":91}#短信发送接口

sms_url= requests.post(server_ip()+'/api/auth/sms',json=sms_data)
print('验证码已发送：',sms_url.text)
#print(sms_url.status_code)
#time.sleep()
#login接口
# login_data={"mobile":"917838381867","code":"123456","phone_code":'91'}
login_data={"mobile":phone_no,"code":"123456","phone_code":'91'}

login_url= requests.post(server_ip()+'/api/auth/login',json=login_data)
print('登录成功：',login_url.text)
#商户新建接口
add_product_Authorization=json.loads(login_url.text)['data']['access_token']
# print('Authorization返回的结果是:',(add_product_Authorization))
add_product_headers={
'Accept-Language': 'zh' ,
'Authorization': 'Bearer '+ add_product_Authorization ,
'Content-Type': 'application/json' ,
'X-UDID': 'qwertyuii'
}
# print(add_product_headers)
add_product_data={
	"name": "timestamp",
	"logo":"",
	"min_amount":200,
	"max_amount":200,
	"min_rate":1.2,
	"max_rate":2.2,
	"url":"http://172.16.40.4:9091/business/?env=inte132&url=http%253A%252F%252F172.16.40.4%253A9091%252Fbusiness%252F%253Fenv%253Dinte132%2523%252Fhome#/edit",
	"intro":"它是接口自动化测试数据",
	"auto":0
}
add_product_url=requests.post(server_ip()+'/api/merchant',json=add_product_data,headers=add_product_headers)
print('商户新建产品返回的结果是',(add_product_url.json()))
#access_token=login_url
#login_token=login_url.json().get('data')
#print(login_token)    {'Content-Type':'application/json','Accept-Language':'zh','token':'login_token'}
#c端首页检查
apply_url=requests.get(server_ip()+'/api/apply')
print('c端首页查询结果：',apply_url.text,apply_url.encoding)
