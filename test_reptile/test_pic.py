# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import re,os
from concurrent import futures
import time

url_mulu="http://www.enterdesk.com/search/1-13-6-0-1920x1080-0"
service_url="http://www.enterdesk.com/download/"
path=os.path.split(os.path.realpath(__file__))[0]
mid_urls=[]
names=[]
id_re=re.compile('<a href="http://www.enterdesk.com/bizhi/(.+).html" target="_blank">(.+)</a>')
scr_re=re.compile('src="(.+)" ')


def getRes(url):
    #result=requests.get("http://www.enterdesk.com/search/%s-13-6-0-1920x1080-0" % num)
    result=requests.get(url)
    return result.text

def getId(res_re,result):

    s=[(num,name)for num,name in re.findall(res_re,result)]
    for j in s:
        temp=service_url+str(j[0])
        mid_urls.append(temp)
        names.append(j[1])



def downloadpic(url,name):
    downloadpage=getRes(url)

    soup=BeautifulSoup(downloadpage,"lxml")
    for m in soup.find_all("div",id="box1"):
        download_url=re.findall(scr_re,str(m))

        respone=requests.get(download_url[0],stream=True)
        with open(path+"\\"+name+".png","wb") as pic :
            for data in respone.iter_content(1024):
                pic.write(data)


def moreProcess(max_worker=4):
    with futures.ProcessPoolExecutor(max_workers=max_worker)as executor:
        executor.map(downloadpic, mid_urls,names)


if __name__=="__main__":
    # for i in range(1,20):
    #     result_mulu=getRes(str(i))
    #     getId(id_re,result_mulu)
    #     print ("===============")
    #     tup=zip(mid_url,names)
    #     for urls,name in tup:
    #         downloadpic(urls,name)
    #
    #         time.sleep(100)

    result_mulu=getRes(url_mulu)
    getId(id_re,result_mulu)
    print ("===============")
    moreProcess()


    # tup=zip(mid_url,names)
    # for urls,name in tup:
    #     downloadpic(urls,name)


