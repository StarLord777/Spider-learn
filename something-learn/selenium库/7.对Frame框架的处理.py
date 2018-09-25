from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')                     #进入一个框架，输入框架的ID
source = browser.find_element_by_css_selector('#draggable')
print(source)
try:
    logo = browser.find_element_by_class_name('logo')#在子框架中获取不到父框架的标签
except NoSuchElementException:
    print('NO LOGO')
browser.switch_to.parent_frame()                            #进入父框架
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)