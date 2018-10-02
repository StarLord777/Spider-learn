import smtplib
from email.mime.text import MIMEText
from email.header import Header
import threading,time

def sendMailToOne():
    print('线程{}正在运行---------------'.format(threading.current_thread().name))
    sender = 'qq@vipjiexi.club'
    receiver = ['1694222672@qq.com']

    msg = MIMEText('邮件测试，本地到QQ邮箱....', 'plain', 'utf-8')
    msg['From'] = Header('qqgageahb1')
    msg['To'] = Header('1694222672@qq.com', 'utf-8')
    msg['Subject'] = Header('python SMTP邮件测试', 'utf-8')

    try:
        smtpobj = smtplib.SMTP('smtp.vipjiexi.club')
        smtpobj.login('qq@vipjiexi.club', 'qjp12345')
        smtpobj.sendmail(sender, receiver, msg.as_string())
        print('发送成功')
        smtpobj.quit()
        smtpobj.close()
    except:
        print('出错了')


if __name__ == '__main__':
    for i in range(20):
        threading.Thread(target=sendMailToOne,).start()
        time.sleep(1)

