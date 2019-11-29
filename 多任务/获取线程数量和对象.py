"""
1.导入threading
2.创建线程对象 threading.Thread()
3.开启子线程start()
"""

import time
import threading


def sing():
    for i in range(5):
        print("正在唱歌。。。", threading.currentThread())  # 获取当前线程对象
        time.sleep(0.5)


def dance():
    for i in range(5):
        print("正在跳舞。。。", threading.currentThread())
        time.sleep(0.5)


if __name__ == "__main__":
    thread_list = threading.enumerate()  # 获取当前活跃的线程列表
    print(len(thread_list), threading.currentThread())

    # sing()
    # dance()
    # 1.导入threading
    # 2.创建线程对象 threading.Thread()
    thread_sing = threading.Thread(target=sing)
    thread_dance = threading.Thread(target=dance)
    thread_list = threading.enumerate()  # 获取当前活跃的线程列表
    print(len(thread_list))
    # 3.开启子线程start()
    thread_sing.start()
    thread_dance.start()
    thread_list = threading.enumerate()  # 获取当前活跃的线程列表
    print(len(thread_list))
