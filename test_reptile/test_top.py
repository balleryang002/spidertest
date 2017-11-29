#coding:utf-8
import requests
import re
import json
from bs4 import BeautifulSoup

post_re = re.compile('\d+\. (.+)\((\d+)\)')
q=[]

def getPostsDetail(input):
    soup= BeautifulSoup(input,"lxml")
    for i in soup.find_all("a"):
        res = list(re.search(post_re, i.text).groups()) + [i['href']]
        q.append(res)
    return q



#http://www.cnblogs.com/mvc/Blog/GetBlogSideBlocks.aspx?blogApp=lovesoo&showFlag=ShowRecentComment%2CShowTopViewPosts%2CShowTopFeedbackPosts%2CShowTopDiggPosts
url="http://www.cnblogs.com/mvc/Blog/GetBlogSideBlocks.aspx"
username="lovesoo"
showTopFlag="ShowTopViewPosts,ShowTopFeedbackPosts,ShowTopDiggPosts"
pram=dict(blogApp=username,showFlag=showTopFlag)
r=requests.get(url,params=pram)
#print (json.dumps(r.json(),ensure_ascii=False))


#a=r.json()["TopViewPosts"]
TopViewPosts =getPostsDetail(r.json()["TopViewPosts"])
TopFeedbackPosts = getPostsDetail(r.json()['TopFeedbackPosts'])
TopDiggPosts = getPostsDetail(r.json()['TopDiggPosts'])

print (json.dumps(dict(TopViewPosts=TopViewPosts, TopFeedbackPosts=TopFeedbackPosts, TopDiggPosts=TopDiggPosts),ensure_ascii=False))