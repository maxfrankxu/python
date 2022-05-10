from bs4 import BeautifulSoup
import urllib.request

url = "https://www.jianshu.com/p/deb8002bbba6"

# define a header to address the error: 'HTTP Error 403: Forbidden'
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
html =response.read()

# 解析网页内容
soup = BeautifulSoup(html, 'html.parser')
usefulurls=[]
pageurls = soup.find_all('a')
for link in pageurls:
    url = link.get('href')
 if url[0:5]!='https':
 pass # 排除不符合要求的网址
 elif len(url)<36:
 pass # 排除不符合要求的网址
 else:
      usefulurls.append(url)

# save urls
import pickle
pickle.dump( usefulurls, open( "./data/usefulurls.p", "wb" ) )


import pickle
# load urls
usefulurls = pickle.load( open( "./data/usefulurls.p", "rb" ) )

import requests
from bs4 import BeautifulSoup
from urllib. parse import urljoin 

body_list = [] # hold all texts
for url in usefulurls:
  user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
  headers={'User-Agent':user_agent,} 
  content = requests.get(url, headers=headers).text

 #获取文章标题
  content = requests. get(url, headers=headers). text
  soup = BeautifulSoup(content, 'lxml')

 #标题
  title = soup.find('h1', class_ ='_1RuRku').text
  body_list.append(title)

 #获取文章正文内容
  body = soup.find('article', class_ ='_2rhmJa')
 for p in body.find_all(['p','h1']):
    sen=p.text.replace(u'\xa0', u'')# delete all '\xa0'
    sen=sen.replace(u'\n', u'') # delete all '\n'
 if len(sen)>1: #delete 空行和只有一个字符的无用行
      body_list.append(sen) 

# save the contend of all urls into a txt file
filename='./data/英语流利说_懂你英语_level1_8.txt'
fileObject = open(filename, 'w')
for text in body_list:
  fileObject.write(text)
  fileObject.write('\n')
fileObject.close()