import requests,time
import my_blog_urls
import nt_nation,nn_nation,nation_http,nation_https

ip_list_yes = []
urls = my_blog_urls.get_urls()      #获取我的博客所有链接
headers = {#创建字典，存储自己浏览器上的信息，从而模拟浏览
    'Cookie':'_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEki'
             'JWIzYzA0ZWNhN2U4YmJiZmI3N2M1YzQ0ZmFjZDU1OGFhBjsAVEkiE'
             'F9jc3JmX3Rva2VuBjsARkkiMXhOSktRWmRoaGlLRXd0UnU1NmtDWT'
             'FvVzh6SVFZUWxTWnlLeGVIVVVpNEU9BjsARg%3D%3D--f0f7b59b27'
             'a7bbb3e87c4eb1f5043c9c5f5ef435; __guid=264997385.176939'
             '6082676313900.1532227595275.8433; Hm_lvt_0cf76c77469e965'
             'd2957f0553e6ecf59=1532227595; monitor_count=5; Hm_lpvt_0'
             'cf76c77469e965d2957f0553e6ecf59=1532227642',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKi'
                 't/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22'
                 '1 Safari/537.36 SE 2.X MetaSr 1.0'
}

#获取所有清洗过的链接并存入ip_list_yes

ip_list_yes = nt_nation.return_ip_list_yes()
print('总计{}个可用ip！*************',{len(ip_list_yes)})

#执行刷访问量服务
def do_to_my_blog():
    n = 1
    num = 1
    while True:
        for i in ip_list_yes:
            print('第{}个代理-----------------------------------'.format(n))
            n = n + 1
            proxies = {'http': 'http://' + i,
                       'https': 'https://' + i}
            for j in urls:
                try:
                    r = requests.get(j, proxies=proxies, headers=headers,timeout = 2)
                    print('浏览成功' + str(num))
                    num += 1
                except:
                    print('出错了')
        time.sleep(65)


do_to_my_blog()