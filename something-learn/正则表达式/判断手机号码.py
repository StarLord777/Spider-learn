import re
'''
正则表达式判断手机号
手机号规则：11位，第一位是1
'''

#普通判断
def judgePhone(num):
    if len(num) != 11 or num[0] != '1':
        return False
    for i in num:
        if i not in '0123456789':
            return False
    return True


print(judgePhone('1694222672'))
print(judgePhone('182346595'))
print(judgePhone('18236548956'))
print(judgePhone('24685135964'))
print(judgePhone('182365S8956'))
print('*'*20)


def re_phone(num):
    if re.match('1\d{10}',num):
        return True
    else:
        return False


print(re_phone('1694222672'))
print(re_phone('182346595'))
print(re_phone('18236548956'))
print(re_phone('24685135964'))
print(re_phone('182365S8956'))
print('*'*20)