''' -*- coding: utf-8 -*-
Create Time: 2020/4/14 8:26 上午
Author:amay
Email:zxm6612719@163.com
File:phone.py
Describe:生成随机手机号码'''
import random
#随机手机号
def get_phone():
   phone_end = ''.join(random.sample('1234567890',10))
   phone_no = '91' + phone_end
   return phone_no
#print(get_phone())