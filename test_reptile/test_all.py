import  requests
import re
import json
from bs4 import BeautifulSoup
from concurrent import futures



def getUser():
    r_user = requests.get('https://www.cnblogs.com/aggsite/UserStats')
    re_user = re.compile('<a href="(http://www.cnblogs.com/.+)" target="_blank">(.+)</a>')
    users = [(url, name) for url, name in re.findall(re_user, r_user.text) if
             "更多推荐博客" not in name and "» 博客列表(按积分)" not in name]
    return users


def getTopView(username):
    url_top = "http://www.cnblogs.com/mvc/Blog/GetBlogSideBlocks.aspx"

    showTopFlag = "ShowTopViewPosts,ShowTopFeedbackPosts,ShowTopDiggPosts"
    pram = dict(blogApp=username, showFlag=showTopFlag)
    r_top = requests.get(url_top, params=pram)

    TopViewPosts = getPostsDetail(r_top.json()['TopViewPosts'])
    TopFeedbackPosts = getPostsDetail(r_top.json()['TopFeedbackPosts'])
    TopDiggPosts = getPostsDetail(r_top.json()['TopDiggPosts'])

    return dict(TopViewPosts=TopViewPosts, TopFeedbackPosts=TopFeedbackPosts, TopDiggPosts=TopDiggPosts)


# def getCategory(username):
#     category_re = re.compile('(.+)\((\d+)\)')
#     url_category = "http://www.cnblogs.com/{0}/mvc/blog/sidecolumn.aspx".format(username)
#     pram = dict(blogApp=username)
#     r_category = requests.get(url_category, params=pram)
#     soup = BeautifulSoup(r_category.text, "lxml")
#     category_all = soup.select('.catListPostCategory > ul > li')
#     category = []
#     for i in category_all:
#         category_res = re.search(category_re, i.text).groups()
#         category.append(category_res)
#     return dict(Category=category)

def getCategory(username):
    category_re = re.compile('(.+)\((\d+)\)')
    url = 'http://www.cnblogs.com/{0}/mvc/blog/sidecolumn.aspx'.format(username)
    blogApp = username
    payload = dict(blogApp=blogApp)
    r = requests.get(url, params=payload)
    soup = BeautifulSoup(r.text, 'lxml')
    category = [re.search(category_re, i.text).groups() for i in soup.select('.catListPostCategory > ul > li') if re.search(category_re, i.text)]

    return dict(Category=category)


def getPostsDetail(post):
    post_re = re.compile('\d+\. (.+)\((\d+)\)')
    result = []
    soup=BeautifulSoup(post,"lxml")
    for i in soup.find_all("a"):
        res = list(re.search(post_re, i.text).groups()) + [i['href']]
        result.append(res)
    return result

def putToghter(username):
    return dict(getTopView(username),**getCategory(username))


def getData(users,max_worker=4):
    with futures.ProcessPoolExecutor(max_workers=max_worker) as executor:
        for blog in executor.map(getCategory,users):

            blogs.append(blog)

def getId(alluser):
    userid=[]

    for i in alluser:
        url=i[0]
        temp=url.split("/")[-2]
        userid.append(temp)
    return userid

def countCategory(category, category_name):
    # 合并计算目录数
    n = 0
    for name, count in category:
        if name.lower() == category_name:
            n += int(count)
    return n


if __name__=="__main__":
    blogs = []
     # a=getCategory("lovesoo")
     # print(a)
    users=getUser()
    print( "一共获取到" +str(len(users))+ "位作者" )

    userid=getId(users)
    getData(userid)
#    print (json.dumps(blogs, ensure_ascii=False))

    new={}
    for i in blogs:
        print(i["Category"])
        for i ,j in i["Category"]:
            if i not in new:
                new[i]=countCategory(i["Category"],i)











