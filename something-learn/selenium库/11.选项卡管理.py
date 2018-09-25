import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')             #通过执行JavaScript来打开一个选项卡，通用方式
print(browser.window_handles)                           #打印所有的窗口信息
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://www.taobao.com')