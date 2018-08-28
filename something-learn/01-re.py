import re
secret_code = 'hadkfalifexxIxxfasdjifja134xxlovexx23345sdfxxyouxx8dfse'
#.*?单独使用
#- .:匹配任意字符，换行符\n除外- *:匹配前一个字符无限次或0次- ?:匹配前一个字符一次或0次
a = re.findall('a.',secret_code)
print(a)
b = re.findall('ad*',secret_code)
print(b)