#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup
import os
maxtrytime=20
rawurl1='https://nomads.ncdc.noaa.gov/data/rucanl/'
local="C:/Users/Yanda_Jiang/Documents/MATLAB/RAP2/"
i=1
a=str(i)
if i<10:
    a='0'+a
rawurl2='2017'+a
os.mkdir(local+rawurl2)
for j in range(1,31):
    b=str(j)
    if j<10:
        b='0'+b
    rawurl3=rawurl2+b
    rawurl=rawurl1+rawurl2+'/'+rawurl3+'/'
    os.mkdir(local+rawurl2+'/'+rawurl3)
    for tries in range(maxtrytime):
        try:
            content = urllib.request.urlopen(rawurl).read().decode('ascii')  #获取页面的HTML
            break;
        except:
            if tries<(maxtrytime-1):
                continue
            else:
                print("has tried "+str(tries)+" times ",rawurl)
#                    logging.error("Has tried %d times to access url %s, all failed!",maxtrytime,url)
                break
    soup = BeautifulSoup(content, 'lxml')
    url_cand_html=soup.find_all('a',href=True) #定位到存放url的标号为content的div标签
    #url_cand_html=soup.find_all("a", string=".grb")
    #list_urls=url_cand_html[0].find_all(".grb") #定位到a标签，其中存放着文件的url
    urls=[]
    
    for i in url_cand_html:
        if i['href'].find('grb')!=-1:
            urls.append(i['href']) #取出链接
    
    seen = set(urls)
    result = []
    for item in urls:
        if item not in seen:
            seen.add(item)
            result.append(item)
    urls=seen
    #for i in url_cand_html:
    #    urls.append(i.get("href"))
    
    for i,url in enumerate(urls):
        print("This is file"+str(i+1)+" downloading! You still have "+str(142-i-1)+" files waiting for downloading!!")
        file_name = local+rawurl2+'/'+rawurl3+'/'+url.split('/')[-1] #文件保存位置+文件名
        url=rawurl+url;
        urllib.request.urlretrieve(url, file_name)
