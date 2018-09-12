import pymysql,time

conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='root',db='allip')
cursor = conn.cursor()

start_time = time.time()
n = 0
a = 0
for b in range(256):
    ips = []
    text = ''
    for c in range(256):
        for d in range(256):
            n += 1
            ip = '{}.{}.{}.{}'.format(a,b,c,d)
            ips.append(ip)
    for i in ips:
        text += '("{}"),'.format(i)
    text = text[:-1]
    sql = 'insert into t1(ip) values {}'.format(text)
    print(sql)
    cursor.execute(sql)
    conn.commit()

end_time = time.time()
print((end_time-start_time)/60)

