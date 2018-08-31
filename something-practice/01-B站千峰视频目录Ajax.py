#B站千峰视频，目录
import requests

url = 'https://api.bilibili.com/x/player/pagelist?aid=17641205&jsonp=jsonp'
headers = {
    'Cookie':'LIVE_BUVID=AUTO3315320820386479; sid=937mixcd; im_notify_typ'
             'e_137652442=0; fts=1532082067; UM_distinctid=164b735150f2d9-06'
             'ef6a8e169184-3c604504-1fa400-164b73515103ea; buvid3=1C951F4B-3'
             '3F5-4681-9B5B-065F1C9759B019887infoc; rpdid=kmpmkkpwlldoskiwqi'
             'oqw; finger=edc6ecda; CURRENT_FNVAL=8; DedeUserID=137652442; De'
             'deUserID__ckMd5=b7f6daf284bfd271; SESSDATA=52ed8301%2C1537845903'
             '%2Ca4ef82c7; bili_jct=768085cd9725b1255c6ab559549f148c; bp_t_off'
             'set_137652442=157578360067349364; CURRENT_QUALITY=64; stardustvi'
             'deo=0; html5_player_gray=false; _dfcaptcha=9bc30570ba1ba333fb036387888cbc00',
    'Host':'api.bilibili.com',
    'Origin':'https://www.bilibili.com',
    'Referer':'https://www.bilibili.com/video/av17641205',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML'
                 ', like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

k_dict = {}

a = requests.get(url,headers=headers).json()

for i in a.get('data'):
    cid = i.get('cid')
    page = i.get('page')
    name = i.get('part')
    d = {
        'cid':cid,
        'page':page,
        'name':name
    }
    k_dict[page] = d

for i,j in k_dict.items():
    print(i,j['name'])