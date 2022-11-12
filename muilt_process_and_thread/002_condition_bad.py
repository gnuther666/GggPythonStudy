from multiprocessing import Condition, Process, Lock
"""
'acquire', 'notify', 'notify_all', 'release', 'wait', 'wait_for'
"""

def write_file(i):
    with open('test_file.txt', 'a') as f:
        f.write(str(i)+ '\n')


def func1(c: Condition, start_num):
    for i in range(start_num, start_num + 10):
        c.acquire(5)
        write_file(i)
        c.release()


def func2(c: Condition, start_num):
    for i in range(start_num, start_num + 10):
        c.acquire(5)
        write_file(i)
        c.release()


if __name__ == '__main__':
    lc = Lock()
    c = Condition()
    p1 = Process(target=func1, args=[c, 0])
    p2 = Process(target=func2, args=[c, 100])
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('进程执行完成')
