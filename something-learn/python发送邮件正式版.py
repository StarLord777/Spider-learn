import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'qq@vipjiexi.club'
receiver = ['1694222672@qq.com']

msg = MIMEText('python邮件测试，本地到QQ邮箱....','plain','utf-8')
msg['From'] = Header('qq','utf-8')
msg['To'] = Header('qq','utf-8')
msg['Subject'] = Header('python SMTP邮件测试','utf-8')


smtpobj = smtplib.SMTP('smtp.vipjiexi.club')
smtpobj.login('qq@vipjiexi.club','qjp12345')
smtpobj.sendmail(sender,receiver,msg.as_string())
