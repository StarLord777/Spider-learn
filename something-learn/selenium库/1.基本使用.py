from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()#声明浏览器对象
try:
    browser.get('https://www.baidu.com')#打开页面
    input = browser.find_element_by_id('kw')#根据ID找到对应的标签，这里是输入框
    input.send_keys('Python')             #输入文字
    input.send_keys(Keys.ENTER)            #模拟回车
    wait = WebDriverWait(browser, 10)      #创建一个等待10秒的对象
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))    #等待直到某个标签加载出来
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()