html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

#print(soup.p.contents)#列表形式，包含所有子节点
#print(soup.p.children)#可迭代形式

#子孙节点
#print(soup.p.descendants)
#for i in enumerate(soup.p.descendants):
#    print(i)

#父节点
#print(soup.title.parent)
#祖先节点
#print(soup.title.parents)
#for i,j in enumerate(soup.title.parents):
#    print(i,j)

#兄弟节点
print(soup.a.previous_sibling)
print(soup.a.next_sibling)
print(soup.a.previous_siblings)
print(soup.a.next_siblings)
