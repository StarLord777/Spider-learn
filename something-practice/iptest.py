import time

start_time = time.time()
n = 0
a = 0
for b in range(255):
    for c in range(255):
        for d in range(255):
            n += 1
            ip = '{}.{}.{}.{}'.format(a,b,c,d)
            print(ip)


end_time = time.time()
print(end_time-start_time)