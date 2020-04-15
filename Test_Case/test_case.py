#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Software
#@Author : amay
#@File : test_case.py
#@Time : 2020/4/14 17:12
import requests
import json
import re
from Config.conf import  *
from Common.get_sql import *
from Common.phone import *

class TestClass:
    def test_send_sms(self):
     phone = get_phone()
     sms_data = {"mobile": phone, "phone_code": 91}  # 短信发送接口
     try:
      sms_url = requests.post(server_ip() + '/api/auth/sms', json=sms_data)
      assert sms_url.status_code == 200
    # print('验证码已发送：',sms_url.text)
     except:
      assert sms_url.status_code != 200
      print('error：验证码发送失败')
     return
    def test_login(self):
     self.test_send_sms('sms_data')['code'] = get_sql('select * from sms order by id desc limit 1')
     login_url = requests.post(server_ip() + '/api/auth/login', json=self.test_send_sms('sms_data'))
     assert 'access_token' in login_url.content.decode('unicode_escape')
