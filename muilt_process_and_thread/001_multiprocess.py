"""
基本的多进程队列通信
"""
from multiprocessing import Process, Queue
import random, time


def product(q):
    for i in range(0, 10):
        q.put('hellow world' + str(i))
        tm = int(random.random() * 10)
        print('生产者休息:' + str(tm))
        time.sleep(tm)


def custom(q):
    for i in range(0, 10):
        ret = q.get()
        print('消费者收到:' + ret)
        tm = int(random.random() * 10)
        print('消费者休息:' + str(tm))
        time.sleep(tm)


if __name__ == '__main__':
    q = Queue()
    print(dir(q))
    p = Process(target=product, args=[q])
    c = Process(target=custom, args=[q])
    p.start()
    c.start()
    p.join()
    c.join()
    print('进程执行完成')
