import re
#re.match()函数   尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
#re.match(pattern, string, flags=0)
print(re.match('www','www.github.com'))     #在起始位置找
print(re.match('git','www.github.com'))     #不在起始位置找，找不到

line = "Cats are smarter than dogs"
mhobj = re.match('(.*) are (.*?) .*?',line)
if mhobj:
    print("match:group():",mhobj.group())
    print("match:group(1):", mhobj.group(1))
    print("match:group(2):", mhobj.group(2))
else:
    print("none")

#re.search()方法      扫描整个字符串并返回第一个成功的匹配。---------------------------
print(re.search('w','www.github.com'))     #在起始位置找
print(re.search('git','www.github.com'))     #不在起始位置找

print(re.search('(.*) are (.*?) .*',line).groups())

#re.sub()       用于检索和替换匹配项
#re.sub(pattern, repl, string, count=0)
phone = "2004-959-559 # 这是一个电话号码"
a = re.sub(' #.*','',phone)
print(a)
num = re.sub('-','',a)
print(num)

#compile 函数 compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
# 供 match() 和 search() 这两个函数使用


#findall() 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
line = 'a1b5c8dfs956sdf482sdfg618geg348'
num = re.findall('\d+',line)
x = re.findall('[a-z]+',line)
print(num)
print(x)