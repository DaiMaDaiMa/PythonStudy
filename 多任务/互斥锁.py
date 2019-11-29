
import threading
import time

num = 0


def work1():
    global num  # 申明 num为全局变量，以下的所有操作都是针对他
    lock.acquire()
    for i in range(1000000):
        num += i
    lock.release()
    print("线程1 中num的值", num)


def work2():
    global num
    lock.acquire()
    for i in range(1000000):
        num += i
    lock.release()
    print("线程2 中num的值", num)


if __name__ == "__main__":
    lock = threading.Lock()
    w1 = threading.Thread(target=work1)
    w2 = threading.Thread(target=work2)
    w1.start()
    # w1.join()  # 礼让线程，让我先执行，缺点是会把多线程变成单线程
    w2.start()
    while len(threading.enumerate()) != 1:
        time.sleep(1)
    print("主线程中num的值 ", num)
