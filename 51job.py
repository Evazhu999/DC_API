# -*- coding: utf-8 -*-
'''@Time    : 2020/4/7 12:03
@Author  : amay
@File    : 51job.py
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
from time import sleep
import re
from lxml import etree
import requests
import os
import json


driver = webdriver.Chrome(chrome_options=chrome_options,executable_path = 'D:\python\chromedriver.exe')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
driver.get("https://search.51job.com/list/020000,000000,0000,00,1,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=01%2C02&cotype=99&degreefrom=03%2C04&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")


#获取cookie
def get_cookie():
    driver.get("https://login.51job.com/login.php?loginway=1&lang=c&url=")
    sleep(2)
    phone=input("输入手机号：")
    driver.find_element_by_id("loginname").send_keys(phone)
    driver.find_element_by_id("btn7").click()
    sleep(1)
    code=input("输入短信：")
    driver.find_element_by_id("phonecode").send_keys(code)
    driver.find_element_by_id("login_btn").click()
    sleep(2)
    cookies = driver.get_cookies()
    with open("cookie.json", "w")as f:
        f.write(json.dumps(cookies))
    driver.close()


#搜索和获得页码
def get_job():
    job = input("输入职位：")
    url=f"https://search.51job.com/list/020000,000000,0000,00,1,99,{job},2,1.html?lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    r=session.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    tree = etree.HTML(r.text)
    x = tree.xpath('//span[@class="td"]/text()')[0]
    total_page = int(re.findall("(\d+)", x)[0])
    href = []
    for i in range(1,total_page+1):
        href.append(re.sub("\d.html", f'{i}.html', url))
    return href


#职位id
def get_job_code(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    r=session.get(url,headers=headers)
    tree=etree.HTML(r.text)
    divs=tree.xpath('//div[@class="el"]/p/span/a/@href')
    job=str(divs)
    job_id=re.findall("\/(\d+).html",job)
    return job_id


#匹配的信息
def get_info(job_id):
    href=f"https://i.51job.com/userset/bounce_window_redirect.php?jobid={job_id}&redirect_type=2"
    r=session.get(href,headers=headers)
    r.encoding=r.apparent_encoding
    tree=etree.HTML(r.text)
    pingjia=tree.xpath('//div[@class="warn w1"]//text()')[0].strip()
    gongsi=[]
    for i in tree.xpath('//div[@class="lf"]//text()'):
        if i.strip():
            gongsi.append(i.strip())
    fenshu=[]
    for i in tree.xpath('//ul[@class="rt"]//text()'):
        if i.strip():
            fenshu.append(i.strip())
    url=f"https://jobs.51job.com/shanghai/{job_id}.html?s=03&t=0"
    return {"公司":gongsi[1],"职位":gongsi[0],"匹配度":pingjia,fenshu[3]:fenshu[2],"链接":url,"_id":job_id}


#用cookie登陆
if not os.path.exists("cookie.json"):
    get_cookie()
f=open("cookie.json","r")
cookies=json.loads(f.read())
f.close()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])


#所有职位id
code=[]
for i in get_job():
    code=code+get_job_code(i)


 #存入Mongo
import pymongo
client=pymongo.MongoClient("47.102.109.190",27017)
db=client["job_zhu"]
job_info=db["job_info"]
for i in code:
    try:
        if not job_info.find_one({"_id":i}):
            info=get_info(i)
            if not job_info.find_one(info):
                job_info.insert_one(info)
                print(info)
                print("插入成功")
    except:

'''print(code)from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
from time import sleep
import re
from lxml import etree
import requests
import os
import json


driver = webdriver.Chrome(chrome_options=chrome_options,executable_path = 'D:\python\chromedriver.exe')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
driver.get("https://search.51job.com/list/020000,000000,0000,00,1,99,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=01%2C02&cotype=99&degreefrom=03%2C04&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=")


#获取cookie
def get_cookie():
    driver.get("https://login.51job.com/login.php?loginway=1&lang=c&url=")
    sleep(2)
    phone=input("输入手机号：")
    driver.find_element_by_id("loginname").send_keys(phone)
    driver.find_element_by_id("btn7").click()
    sleep(1)
    code=input("输入短信：")
    driver.find_element_by_id("phonecode").send_keys(code)
    driver.find_element_by_id("login_btn").click()
    sleep(2)
    cookies = driver.get_cookies()
    with open("cookie.json", "w")as f:
        f.write(json.dumps(cookies))
    driver.close()


#搜索和获得页码
def get_job():
    job = input("输入职位：")
    url=f"https://search.51job.com/list/020000,000000,0000,00,1,99,{job},2,1.html?lang=c&stype=1&postchannel=0000&workyear=02&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=5&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    r=session.get(url,headers=headers)
    r.encoding=r.apparent_encoding
    tree = etree.HTML(r.text)
    x = tree.xpath('//span[@class="td"]/text()')[0]
    total_page = int(re.findall("(\d+)", x)[0])
    href = []
    for i in range(1,total_page+1):
        href.append(re.sub("\d.html", f'{i}.html', url))
    return href


#职位id
def get_job_code(url):
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"}
    r=session.get(url,headers=headers)
    tree=etree.HTML(r.text)
    divs=tree.xpath('//div[@class="el"]/p/span/a/@href')
    job=str(divs)
    job_id=re.findall("\/(\d+).html",job)
    return job_id


#匹配的信息
def get_info(job_id):
    href=f"https://i.51job.com/userset/bounce_window_redirect.php?jobid={job_id}&redirect_type=2"
    r=session.get(href,headers=headers)
    r.encoding=r.apparent_encoding
    tree=etree.HTML(r.text)
    pingjia=tree.xpath('//div[@class="warn w1"]//text()')[0].strip()
    gongsi=[]
    for i in tree.xpath('//div[@class="lf"]//text()'):
        if i.strip():
            gongsi.append(i.strip())
    fenshu=[]
    for i in tree.xpath('//ul[@class="rt"]//text()'):
        if i.strip():
            fenshu.append(i.strip())
    url=f"https://jobs.51job.com/shanghai/{job_id}.html?s=03&t=0"
    return {"公司":gongsi[1],"职位":gongsi[0],"匹配度":pingjia,fenshu[3]:fenshu[2],"链接":url,"_id":job_id}


#用cookie登陆
if not os.path.exists("cookie.json"):
    get_cookie()
f=open("cookie.json","r")
cookies=json.loads(f.read())
f.close()
session = requests.Session()
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])


#所有职位id
code=[]
for i in get_job():
    code=code+get_job_code(i)


 #存入Mongo
import pymongo
client=pymongo.MongoClient("47.102.109.190",27017)
db=client["job_zhu"]
job_info=db["job_info"]
for i in code:
    try:
        if not job_info.find_one({"_id":i}):
            info=get_info(i)
            if not job_info.find_one(info):
                job_info.insert_one(info)
                print(info)
                print("插入成功")
    except:
        print(code)