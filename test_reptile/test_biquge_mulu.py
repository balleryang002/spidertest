# -*- coding:UTF-8 -*-

import requests
import re
from bs4 import BeautifulSoup

server = 'http://www.biqukan.com/'
url="http://www.biqukan.com/0_790/"
list=[]

res=requests.get(url)
#<dd><a href="/0_790/16802270.html">第一百三十章 骄子楼</a></dd>
re_res='<dd><a href="(.+)">(.+)</a></dd>'
s=[(url,name)for url,name in re.findall(re_res,res.text)]
for i in s :
    each=server+i[0]
    list.append(each)

print (list[16:])

# print ("========================================")
# soup=BeautifulSoup(res.text,"lxml")
# for i in soup.select('.listmain a '):
#     print (i)



for j in list[16:]:
    re_text=requests.get(j)
    respone=re.get(re_text)


# def writeIn():
#     with open()as f:


