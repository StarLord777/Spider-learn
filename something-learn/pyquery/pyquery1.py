from pyquery import PyQuery

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
ht = PyQuery(html)
#print(ht('li'))     #直接传入CSS选择器

#print(ht('#container .list .item-1'))

#子，父
#print(ht.find('.item-1').children())
#print(ht.find('.item-1').parent())

#兄弟节点
#print(ht('.item-1.active').siblings())

#遍历
#for i in ht('li').items():
#    print(i)
#print(type(ht('li').items()))       #生成器对象

#---------------------------------------------------------------------
#获取内容
#print(ht('.item-1.active a').attr('href'))
#print(ht('.item-1.active a').text())
#print(ht('.item-1.active').html())      #获取除去本级标签的内容