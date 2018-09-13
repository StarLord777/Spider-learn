html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
#print(soup.prettify())
#print(soup.title.string)

#print(soup.head)
#print(soup.head.title)
#print(type(soup.head))

#print(soup.body.a)
#获取标签名称
#print(soup.title.name)

#获取标签的属性
#print(soup.body.p['class'])
#print(soup.body.p['name'])


#获取标签的内容
print(soup.p.string)
print(soup.p.text)