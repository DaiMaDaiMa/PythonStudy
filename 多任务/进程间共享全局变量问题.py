"""
结论：进程间是不能共享全局变量的。子进程若想修改全局变量都要使用global关键字申明，否则只能访问，不能修改
进程间修改全局变量，相当于拷贝了一份在自己的进程中，但对原始的全局变量没有影响。（维持原值）
向进程传递参数值方法和多线程一样
"""


import multiprocessing
 
g_num = 10


def work1():
    global g_num
    for i in range(10):
        g_num += 1
    print("work1   ", g_num)


def work2():
    global g_num
    for i in range(5):
        g_num += 1
    print("work2...", g_num)


if __name__ == "__main__":

    mp1 = multiprocessing.Process(target=work1)
    mp2 = multiprocessing.Process(target=work2)
    mp1.start()
    mp2.start()
    for i in range(20):
        g_num += 1

    print("main.....", g_num)
