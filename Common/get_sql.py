#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Software
#@Author : amay
#@File : get_sql.py
#@Time : 2020/4/13 13:05
import pymysql
from Config.conf import sql_conf #导入数据库连接的参数
def get_sql(sql):
    #建立一个连接对象
  host,user,password,port,database,charset=sql_conf()#导入的值保存在变量里面
  db = pymysql.connect(host=host,user= user,password =password,port = port,database=database,charset =charset)
    #cursorclass = pymysql.cursors.DictCursor # 设置游标类型,已返回不同类型数据
      #建立一个游标
  cursor = db.cursor()
      #运行sql语句
  cursor.execute(sql)
      #把sql运行的数据保存在data变量里面
  data=cursor.fetchall()#获取查询所有的值
  cursor.close()#关闭游标
  db.close()#关闭数据库连接
  return data
#print(get_sql('select id from merchant_product order by  id desc limit 1'))#运行的sql语句

