import qrcode as qr
import qrdecode as dqr
import ybc_box as box
import ybc_speech as sp

import random as ran
import os
import requests as req

sp.speak('''
胡展铭同学 精品
胡展铭同学的作业很认真哦，讲解视频有10分钟呢~现在老师就来批改一下你的作业吧

本节课主要学习了二维码这个第三方库的使用，分为生成二维码库（qrcode）和二维码解码库（qrdecode），依赖于Image库（可以通过安装pillow库的方式）。（几乎每天都要用到的东西已经被我们的同学掌握原理了）
''')
while True:
    op = box.buttonbox('请问您需要什么操作？',['生成官网二维码','二维码生成','二维码识别','退出'])
    if op == '退出':
        break
    elif op == '生成官网二维码':
        box.msgbox('正在生成，\n进度0%')
        url = 'https:\\www.yuanfudao.com'
        obj = qr.make(url)
        obj.show()
        obj.save('1.jpg')
        box.msgbox('正在生成，\n进度80%')
        box.msgbox('生成完毕')
    elif op == '二维码生成':
        ops = box.buttonbox('选择二维码类型',['文本类','网址类'])
        if ops == '文本类':
            box.msgbox('正在初始化，请稍等')
    elif op == '二维码识别':
        obj = dqr.decode('1.jpg')
        box.msgbox(obj)

