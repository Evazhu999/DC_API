''' -*- coding: utf-8 -*-
Create Time: 2020/4/8 7:46 上午
Author:amay
Email:zxm6612719@163.com
File:get_excel.py
Describe:'获取excel数据'''
import xlrd # 导入excel操作的包
excel=xlrd.open_workbook('../TestData/usermeassage.xlsx')#打开文件，文件的地址要用相对路径
table=excel.sheets()[0]#读取第一页的信息，0表示第一个，1表示第二页
print(table.nrows) #取总的行数
print(table.ncols)#取总的列数
print(table.rows_values(0))#取第一行的数据
print(table.col_values(0))#取第一列的数据
print(table.cell_values(0,1))#取第一行第一列的数据，前面是行后面是列
for i in range(1,table.nrows):
    print(table.cell_values(i,1),table.cell_values(i,2))bang
    'zuibang'