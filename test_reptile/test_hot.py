#coding:utf-8
import requests
import re
import json

r=requests.get('https://www.cnblogs.com/aggsite/UserStats')
#print (r.text)

#<li>72. <a href="http://www.cnblogs.com/zjutlitao/" target="_blank">beautifulzzzz</a></li>
re_user=re.compile('<a href="(http://www.cnblogs.com/.+)" target="_blank">(.+)</a>')
users=[(url,name)for url,name in re.findall(re_user,r.text) if "更多推荐博客" not in name and "» 博客列表(按积分)" not in name]
print (json.dumps(users,ensure_ascii=False))