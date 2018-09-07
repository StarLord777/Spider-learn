'''
1.字符串切割
re.split

'''
import re
str = 'you    need   python'
print(str.split(' '))
print(re.split(' +',str))
print('*'*80)

#re.finditer    与findall效果一样，只不过是返回一个迭代器，

a = re.finditer('\d{3}','4864646756')
print(a)
for i in a:
    print(i.group())

print('*'*80)


'''
#字符串的修改和替换，re.sub,re.subn
参数：
pattern :re 表达式
repl:       用来替换的字符串
string:     要被替换的字符串
count:      指定替换次数
flags:          同正常意思

#sub与subn区别，前者返回一个字符串，后者返回一个元组,第一个参数是返回的字符串，第二个参数是替换的次数
'''

print(re.sub('\d','*','str123python 456 haha 7'))
print(re.subn('\d','*','str123python 456 haha 7'))

'''
分组的概念，()，爬虫常用


'''
a = re.findall('(\d+)2','182 32 4562 7829')
print(a)
b = re.findall('(.*?)a(a)','hahaaa,pythaa woaa ')
print(b)

c = re.findall('(?P<num>\d{3}).*?(?P<ha>\d{5})','123-1654849879')
print(c)


'''
对正则表达式进行编译，以后用方便
'''
findnum = re.compile('\d+')

print(findnum.findall('sajdf546841561safdg35465'))

'''
练习：判断QQ号，判断邮箱，判断IP，
'''

str = '1694222672  haha 1694222672@qq.com,smk@163.com666 777 192.18.7.0'
qq = print(re.findall('\d{4,10}',str))      #贪婪匹配，连着的四个到10个数字

email = print(re.findall('\w+@.*?com',str))     #  \w   匹配数字字母下划线

ip = print(re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',str))    #     .  需要被转义

