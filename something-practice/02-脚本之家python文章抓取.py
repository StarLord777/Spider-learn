import requests
from bs4 import BeautifulSoup


url = 'https://www.jb51.net/list/list_97_1.htm'
response = requests.get(url)
#print(dir(response))
#print(response.encoding)
response.encoding = 'gb2312'
html = response.text
soup = BeautifulSoup(html,'lxml')
txt = soup.select('div.artlist dl dt')
#print(txt)
href_list = []
base_url = 'https://www.jb51.net'

for i in txt:
    title = i.select('a')[0]['title']
    href = base_url + i.select('a')[0]['href']
    print(href,title)
    href_list.append(href)

