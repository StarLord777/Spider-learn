from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')

input_1 = browser.find_element_by_id('q')
input_2 = browser.find_element_by_css_selector('#q')
input_3 = browser.find_element_by_class_name('search-combobox-input')
print(input_1)
print(input_2)
print(input_3)

'''
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
'''