import urllib.request
from pyquery import PyQuery as pq
import os

def HttpClient(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url,headers = headers)
    response = urllib.request.urlopen(req)
    html=pq(response.read().decode("utf-8"))
    return html


cc=0
os.mkdir("Data")

for p in range(1,60):

    if p==1:
        url="http://qq.yh31.com/zjbq/0551964.html"
    else:
        url="http://qq.yh31.com/zjbq/0551964_"+str(p)+".html"

    html=HttpClient(url)
    imglist=html.find("#fontzoom").find("img")
    for x in imglist.items():
       try:
        imgurl="http://qq.yh31.com/" + x.attr("src")
        imgsrc=x.attr("src").replace("/","")
        nickurl="Data/"+ imgsrc[9:]
        urllib.request.urlretrieve(imgurl,nickurl)
        cc+=1
        print(nickurl+"已成功抓取.........")
        print("                                         ")
       except Exception:
           ee="error"
        
     

print("抓取完成，一共抓取了"+str(cc)+"张表情图")


