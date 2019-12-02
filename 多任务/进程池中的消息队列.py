import multiprocessing
import time


def write(queue):
     # for循环，向队列写入数据
    for i in range(10):
        # 判断队列是否已满
        if queue.full():
            print("队列已满!")
            break
        # 向队列中放入值
        queue.put(i)
        print("写入成功，已经写入:", i)
        time.sleep(0.5)


def read(queue):
    while True:

        # 判断队列是否已经为空
        if queue.qsize() == 0:
            print("队列已空!")
            break

        # 从队列中读取数据
        value = queue.get()
        print("已经读取:", value)


if __name__ == "__main__":
    pool = multiprocessing.Pool(2)
    queue = multiprocessing.Manager().Queue()

    # 3、使用进程池执行任务

    #     3.1 同步方式
    # pool.apply(write_queue, (queue, ))
    # pool.apply(read_queue, (queue, ))

    #     3.2 异步方式
    # apply_async() 返回值 ApplyResult对象，该对象由一个 wait() 的方法
    # wait() 方法类似join() 表示先让当前进程执行完毕，后续进程才能启动
    # 异步
    pool.apply_async(write, (queue, )).wait()

    pool.apply_async(read, (queue, ))
    pool.close()
    pool.join()

    # 同步
