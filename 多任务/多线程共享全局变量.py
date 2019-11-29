

"""
在⼀个进程内的所有线程共享全局变量，很⽅便在多个线程间共享数据
在⼀个进程内的所有线程共享全局变量，很⽅便在多个线程间共享数据 缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量的混乱（即线程⾮安全）
"""


import threading
import time

num = 0


def work1():
    global num  # 申明 num为全局变量，以下的所有操作都是针对他
    for i in range(10):
        num += i
    print("线程1 中num的值", num)


def work2():
    global num
    # num = 100  # 若局部变量含有同名参数，就近原则，使用局部变量
    # time.sleep(3)
    print("线程2中num的值 ", num)


if __name__ == "__main__":
    w1 = threading.Thread(target=work1)
    w2 = threading.Thread(target=work2)
    w1.start()
    w2.start()
    while len(threading.enumerate()) == 1:
        time.sleep(2)
    print("主线程中num的值 ", num)
