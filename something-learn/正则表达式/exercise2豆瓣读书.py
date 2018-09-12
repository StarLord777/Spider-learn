import requests
import re

url = 'https://book.douban.com/tag/?view=type'
tag_dict = {}

def get_dict():             #接口，提供这个标签字典
    return tag_dict

r = requests.get(url).text
tag_title = re.findall('<a name="(.*?)".*?tag-title-wrapper', r, re.S)  #直接找到类别
tags = re.findall('table.*?tbody>(.*?)</tbody',r,re.S)  #找到每个div里tbody的内容
tags.remove(tags[0])
for n,i in enumerate(tags):
    tag_list = re.findall('">(.*?)</a><b',i,re.S)   #在tbody里找到每个a标签的内容
    tag_dict[tag_title[n]] = tag_list

for i in tag_dict:
    print(i,tag_dict[i])