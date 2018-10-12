import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading,time
import redis
redis = redis.Redis(db=15)



def sendMailToOne():
    print('线程{}正在运行---------------'.format(threading.current_thread().name))
    sender = '001@vipjiexi.club'
    receiver = ['2492057915@qq.com']
    #receiver = []
    #获取接收人



    msg = MIMEText('悉心收集，包括但不限于英语(各种考试，口语),计算机(编程，网络安全，硬件创客)'
                   ',绘画,健身，vip电影电视剧音乐等', 'plain', 'utf-8')
    msg['From'] = Header('001')
    msg['To'] = Header('爱学习的您', 'utf-8')
    msg['Subject'] = Header('如果您需要任何类别的学习资料，请联系我', 'utf-8')

    try:
        smtpobj = smtplib.SMTP('smtp.vipjiexi.club')
        smtpobj.login('001@vipjiexi.club', 'qjp12345')
        smtpobj.sendmail(sender, receiver, msg.as_string())
        print('发送成功')
        smtpobj.quit()
        smtpobj.close()
    except Exception as e:
        print('{}-----出错了'.format(e))


if __name__ == '__main__':
    for i in range(20):
        threading.Thread(target=sendMailToOne,).start()
        time.sleep(1)