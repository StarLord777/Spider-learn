from selenium import webdriver
from selenium.webdriver import ActionChains

#模拟拖拽
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')                     #切换到内部的iframe框架
source = browser.find_element_by_css_selector('#draggable') #选择源
target = browser.find_element_by_css_selector('#droppable') #选择目标
print(source,target)
actions = ActionChains(browser)                             #创建动作链对象
actions.drag_and_drop(source, target)                       #设计动作
###重点
actions.perform()#开始你的表演