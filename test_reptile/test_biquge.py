# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os
from concurrent import futures

path=os.path.split(os.path.realpath(__file__))[0]
service_url= 'http://www.biqukan.com'
request_url="http://www.biqukan.com/0_790/"
urls=[]
names=[]


# def writein(name,text):
#     rpath=path + "\\"+ name +".txt"
#     with open(rpath,"a",) as f:
#         f.writelines(text)


def getMulu():
    res=requests.get(request_url)
    re_res = '<dd><a href="(.+)">(.+)</a></dd>'
    s = [(url, name) for url, name in re.findall(re_res, res.text)]
    for i in s:
        each_url = service_url + i[0]
        urls.append(each_url)
        each_name=i[1]
        names.append(each_name)

def getdownload(name,url):
    res_down=requests.get(url)
    soup=BeautifulSoup(res_down.text,"lxml")
    texts = soup.find_all('div', class_='showtxt')
    f_texts = texts[0].text.replace('\xa0' * 8, '\n\n')
    r_path=path + "\\"+ name +".txt"
    with open(r_path,"a",encoding='utf-8') as f:
        f.writelines(f_texts)

# def getreptile(max_worker=4):
#     with futures.ProcessPoolExecutor(max_workers=max_worker)as executor:
#         for each_item in executor.map(getdownload,urls):


if __name__=="__main__":
    getMulu()
    f_url=urls[16:]
    f_name=names[16:]


    print("================")
    m=zip(f_name,f_url)
    for name,url in m :
        getdownload(name,url)










