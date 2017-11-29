#coding:utf-8
import requests
import re
import json
from bs4 import BeautifulSoup

username="lovesoo"
url="http://www.cnblogs.com/{0}/mvc/blog/sidecolumn.aspx".format(username)
category=[]
#?blogApp=lovesoo
pram=dict(blogApp=username)
r=requests.get(url,params=pram)

#u'使用BeautifulSoup先找到对应的节点，再二次搜索
#<a id="CatList_LinkList_0_Link_0" href="http://www.cnblogs.com/lovesoo/category/1102003.html">jmeter(3)</a>
category_re = re.compile('(.+)\((\d+)\)')
soup=BeautifulSoup(r.text,"lxml")
category_all=soup.select('.catListPostCategory > ul > li')
for i in category_all:

    category_res=re.search(category_re,i.text).groups()
    category.append(category_res)

print(json.dumps(category, ensure_ascii=False))



