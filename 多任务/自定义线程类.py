"""
1.创建子类继承自threading.Thread
2.重写run()方法
3.子类对象调用start()方法
"""

import threading
import time


class myThread(threading.Thread):

    def __init__(self, num):
        super().__init__()  # 重写父类初始化方法，要先调用父类初始化方法

        self.num = num

        print("我是子类初始化方法", num)

    def run(self):
        for i in range(5):
            print("我是子类，运行第 %d 次" % i)
            time.sleep(0.5)


if __name__ == "__main__":

    mt = myThread(10)
    mt.start()
