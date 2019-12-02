import multiprocessing


def send(queue):
    if queue.full():
        print("队列已满")
        return
    for i in range(10):
        queue.put(i)
        print("已存入：", i)


def recv(queue):
    while True:
        if queue.qsize() == 0:
            print("队列已空")
            break
        print("取出：", queue.get())


if __name__ == "__main__":

    queue = multiprocessing.Queue()
    sp = multiprocessing.Process(target=send, args=(queue, ))
    rp = multiprocessing.Process(target=recv, args=(queue, ))
    sp.start()
    sp.join()
    rp.start()
