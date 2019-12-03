"""
在单线程中实现多任务。当一个任务等待，阻塞等状态时，自动的切换到另一个任务
"""

import time
def work1():
    while True:
        print("work1正在工作。。。")
        time.sleep(0.5)
        yield


def work2():
    while True:
        print("work2正在工作。。。")
        time.sleep(0.5)
        yield


if __name__ == "__main__":
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)
