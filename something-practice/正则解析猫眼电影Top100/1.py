import requests,re

base_url = 'http://maoyan.com/board/4?offset={}'
urls = []
for i in range(10):
    urls.append(base_url.format(10*i))

#构造headers
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie':'__mta=251008569.1536744988778.1536745503768.1536745544944.17; _lxsdk_cuid=165cd22f1a0c8-0ec18267a3a2f5-3c604504-1fa400-165cd22f1a0c8; uuid_n_v=v1; uuid=53511D10B66F11E894F593DFAB82C37F1716AA64EB0848C2BADBC75AA2E23EA6; _csrf=5f3373e2e85bd09c75c54ffbc624db254862d2ceb2dfbeff81eb9fa58e289001; __guid=17099173.3022114119644780000.1536744988414.424; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk=53511D10B66F11E894F593DFAB82C37F1716AA64EB0848C2BADBC75AA2E23EA6; __mta=251008569.1536744988778.1536744999954.1536745003054.4; monitor_count=17; _lxsdk_s=165cd22f1a1-995-e6-849%7C%7C47'
}
def get_onepage(url):
    response = requests.get(url,headers=headers).text
    print(response)
    print(re.findall('<a',response,re.S))


get_onepage(urls[0])
