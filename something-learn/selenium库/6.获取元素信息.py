#获取元素的属性
from selenium import webdriver

browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))


#获取元素的文本
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)

#获取ID，位置，标签名，大小
print(input.id)
print(input.location)
print(input.size)
print(input.tag_name)
