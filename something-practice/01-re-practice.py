#找出中国大学MOOC中所有课程的标题，链接和图片地址，存入字典中
import re,requests
url = 'https://www.52pojie.cn/'

html = requests.get(url).text
print(html)

