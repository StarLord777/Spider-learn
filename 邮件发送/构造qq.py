#构造6位所有qq号
import redis
redis = redis.Redis(db=15)


#第一个可以是1开头，其余位可以是0
def qq6():
    for i1 in range(1, 10):
        for i2 in range(0, 10):
            for i3 in range(0, 10):
                for i4 in range(0, 10):
                    for i5 in range(0, 10):
                        for i6 in range(0, 10):
                            str = '{}{}{}{}{}{}@qq.com'.format(i1, i2, i3, i4, i5, i6)
                            redis.rpush('qq6', str)
                    redis.rpush('qq6','1694222672@qq.com')


qq6()