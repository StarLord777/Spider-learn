#re

'''
re.match(re,str,flags)
参数：表达式，字符串
作用：从字符串开始匹配，如果不是起始位置匹配成功，返回None

re.I    忽略大小写
re.M    多行匹配，影响   ^  $
re.S    使  .  匹配包括换行符在内的所有字符
re.U    根据Unicode字符集解析，影响\w,\W,\b,\B
re.X
'''
import re

print(re.match('www','www.baidu.com'))
print(re.match('www','ww.baidu.com'))
print(re.match('ww','www.baidu.com'))
print(re.match('www','wWw.baidu.com'))
print(re.match('www','wWw.baidu.com',re.I))
print(re.match('www','.baiwwwdu.com'))

print('*'*80)
#----------------------------------------------------------------------------------------------
'''
re.search()
作用：扫描整个字符串，返回第一个成功的匹配
'''
print(re.search('www','www.baidu.com'))
print(re.search('www','.baiwwwdu.com'))
print('*'*80)

#----------------------------------------------------------------------------------------------
'''
re.findall()
作用：找到所有符合的匹配项
'''

print(re.findall('ww','haha,ww,ww,python ,666,ww'))

