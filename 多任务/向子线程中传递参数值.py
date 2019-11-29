"""
1.导入threading
2.创建线程对象 threading.Thread()
3.开启子线程start()
"""

import time
import threading


def sing(a, b, c):
    for i in range(5):
        print("正在唱歌。。。")
        print("参数：", a, b, c)
        time.sleep(0.5)


def dance():
    for i in range(5):
        print("正在跳舞。。。")
        time.sleep(0.5)


if __name__ == "__main__":

    # sing()
    # dance()
    # 1.导入threading
    # 2.创建线程对象 threading.Thread()
    # thread_sing = threading.Thread(target=sing, args=(100, 1000, 10000))  # 使用元组赋值
    # thread_sing = threading.Thread(target=sing, kwargs={"a": 10, "c": 10000, "b": 1000})  # 使用字典赋值 但是键一定要相同
    thread_sing = threading.Thread(target=sing, args=(
        100, 1000), kwargs={"c": 10000})   # 混合使用赋值

    thread_dance = threading.Thread(target=dance)
    # 3.开启子线程start()
    thread_sing.start()
    thread_dance.start()
