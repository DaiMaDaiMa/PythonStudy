import time
import multiprocessing


def work():
    print("正在复制：", multiprocessing.current_process().name)
    time.sleep(0.5)


if __name__ == "__main__":
    # 2、创建一个进程池，长度3，（表示进程池中最多能够创建3个进程）
    # 进程池创建，有两步:
    # 1)导入模块
    # 2）创建进程池  multiprocessing.Pool(2)  最大允许创建2个进程
    # 3、先用进程池同步方式拷贝文件
    # pool.apply(函数名, (传递给函数的参数1,参数2,....))
    # pool.apply(copy_work)
    # 4、再用进程池异步工作方式拷贝文件
    # 如果使用 apply_async 方式，需要做2点：
    # 1）pool.close() 表示不在接收新的任务
    # 2）主进程不在等待进程池执行结束后在退出，需要进程池join()
    #   pool.join() 让主进程等待进程池执行接收后再退出
    pool = multiprocessing.Pool(3)
    for i in range(10):

        # pool.apply(work)
        pool.apply_async(work)
    pool.close()  # close 表示不再接收新的任务
    pool.join()  # 让主进程等待进程池执行完后再退出
