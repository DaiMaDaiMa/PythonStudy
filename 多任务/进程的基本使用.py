"""
1.导入模块
2.创建子进程对象
3.开启子进程
4.multiprocessing.current_process()  获取当前进程  .name 获取当前进程的名称 .pid获取当前进程的pid
5.也可以通过os模块的getpid getppid 方法获取pid
6.杀死进程kill -9 进程编号
"""
import time
import multiprocessing
import os


def work():
    for i in range(10):
        print("子进程正在运行。。。")
        print(multiprocessing.current_process().name)  # 获取的是子进程对象的名称
        print("获取子进程id:", os.getpid(), "获取父进程id",
              os.getppid())  # 获取子进程pid和父进程pid
        time.sleep(0.5)


if __name__ == "__main__":
    print(multiprocessing.current_process().name)  # 　获取主进程名称
    print(multiprocessing.current_process().pid)  # 　获取主进程pid
    mp = multiprocessing.Process(target=work, name="p1")
    mp.start()
    # print(mp.name)  # 获取子进程名称
    print(mp.pid)  # 获取子进程pid
    # for i in range(10):
    #     print("主进程正在运行。。。")
    #     time.sleep(0.5)
