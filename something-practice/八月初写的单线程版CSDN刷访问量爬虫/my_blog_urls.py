import requests
from bs4 import BeautifulSoup

url = 'https://blog.csdn.net/q1694222672'
url2 = 'https://blog.csdn.net/q1694222672/article/list/2'
url3 = 'https://blog.csdn.net/q1694222672/article/list/3'
urls=[]

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
for i in soup.select('div h4 a'):
    urls.append(i['href'])

r2 = requests.get(url2)
soup = BeautifulSoup(r2.text,'lxml')
for i in soup.select('div h4 a'):
    urls.append(i['href'])

r3 = requests.get(url3)
soup = BeautifulSoup(r3.text,'lxml')
for i in soup.select('div h4 a'):
    urls.append(i['href'])

for i in urls:
    print(i)

print(len(urls))

def get_urls():
    return urls