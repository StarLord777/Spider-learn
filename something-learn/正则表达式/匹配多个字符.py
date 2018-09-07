'''
(abc)是一个整体
x?  匹配0个或者1个x
x*  匹配0个或者任意个x
x+  至少匹配一个x
x{n}    匹配确定的n个x    x{n,}   匹配至少n个x
'''
import re

print(re.findall('(python)','python1python2python3python4'))
print(re.findall('(ab?)','1ab2a3b 7abc 8 bbb'))
print(re.findall('(x(ab)?)','1xab2xa3xb 7xabc 8 xbbb'))

print(re.findall('ab*','1a 2ab 3a b 4abbbb 5bbb 6aaa'))
print(re.findall('\d{3}','169 a4222 b67'))
print(re.findall('a+','1abc 2aa 3bac'))
print('*'*80)
#.*是贪婪匹配，.?是非贪婪匹配
print(re.findall('.*','sajkfdl'))
print(re.findall('.?','sajkfdl'))

#  a|b  匹配x或y
print(re.findall('a|b','a35b78c78ab'))


#需求：提取 I.....you
str = 'I love you I see you I hate you I found you I pick you I lose you I give you'
print(re.findall('I.*?you',str))

