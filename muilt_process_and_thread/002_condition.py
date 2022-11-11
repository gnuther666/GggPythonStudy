from multiprocessing import Condition, Process
"""
'acquire', 'notify', 'notify_all', 'release', 'wait', 'wait_for'
"""

def func1(c: Condition, start_num):
    for i in range(start_num, start_num + 10):
        print(i)
        c.release()


def func2(c: Condition, start_num):
    for i in range(start_num, start_num + 10):
        print(i)
        c.release()


if __name__ == '__main__':
    c = Condition()
    c.acquire()
    p1 = Process(target=func1, args=[c, 0])
    p2 = Process(target=func2, args=[c, 100])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('进程执行完成')
