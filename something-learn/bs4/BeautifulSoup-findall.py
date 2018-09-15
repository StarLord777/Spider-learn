html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
#print(soup.find_all('ul'))
#print(type(soup.find_all('ul')[0]))

#根据属性
#print(soup.findAll(id='list-2'))
#print(soup.findAll(class_='element'))
#print(soup.findAll(attrs={'class':'list'}))

#根据文本
#print(soup.findAll(text='Bar'))

#print(soup.find(class_='element'))

#CSS选择器
#print(soup.select('.panel .panel-heading'))
#print(soup.select('ul li'))
#print(soup.select('ul#list-2 li'))

for i in soup.select('ul'):
    print(i['id'],i['class'])
    print(i.get_text)

