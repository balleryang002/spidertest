import urllib.request


url="https://www.zhihu.com/api/v4/announcement"
agent="Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
auth={}
header={"User-Agent":agent}

re=urllib.request.urlopen()