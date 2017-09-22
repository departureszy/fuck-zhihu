
# coding: utf8

import requests
from bs4 import BeautifulSoup
import os, time
import re
import http.cookiejar as cookielib
from selenium import webdriver
from lxml import etree


# 构造 Request headers
agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'
headers = {
    "Host": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    'User-Agent': agent,
    'X-Requested-With':'XMLHttpRequest'
}

######### 构造用于网络请求的session
session = requests.Session()
session.cookies = cookielib.LWPCookieJar(filename='zhihucookie')
try:
    session.cookies.load(ignore_discard=True)
except:
    print('cookie 文件未能加载')

############################判断是否登录成功
profileurl = 'https://www.zhihu.com/settings/profile'
profileresponse = session.get(url=profileurl, headers=headers)
print('profile页面响应码：', profileresponse.status_code)
if profileresponse.status_code==200:
    print("登录成功啦")

# profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
# div = profilesoup.find('div', {'id': 'rename-section'})
# print(div)
topicurl="https://www.zhihu.com/topics"
topicresponse=session.get(url=topicurl,headers=headers)

driver=webdriver.PhantomJS()
driver.get("https://www.zhihu.com/topics")
topic=[]

print()
while driver.page_source.__contains__("</div><a aria-role=\"button\" class=\"zg-btn-white zu-button-more\">更多</a>"):

    # selenium 模拟点击更多按钮

    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/a[1]").click()
    time.sleep(1)
    # topicsoup=BeautifulSoup(driver.page_source,'html.parser')
    # data=topicsoup.findChildren('ul',{'class':'zm-topic-cat-main clearfix'})
    # for i in data:
    #     topic=re.findall("<a href=\"#.*?\">(.*?)</a>",str(i))
    #     print(topic)
    topic.append(re.findall("<strong>(.*?)</strong>",driver.page_source))
    # print(driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div[2]/a").__sizeof__())
    print(topic)
driver.close()