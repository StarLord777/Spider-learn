import requests,json

base_url = 'https://www.toutiao.com/search_content/?offset={}&format=json&keyword=%E8%A1%97%E' \
      '6%8B%8D&autoload=true&count=20&cur_tab=1&from=search_tab'
def get_onepage(url):
    jtxt = requests.get(url).json()
    for i in jtxt['data']:
        print(i)

#构造链接
urls = []
for i in range(10):
    urls.append(base_url.format(i*20))

#测试单页
get_onepage(urls[0])