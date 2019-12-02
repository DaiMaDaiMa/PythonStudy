import multiprocessing

queue = multiprocessing.Queue()
queue.put(1)
queue.put(1)
queue.put(1)
print(queue.qsize())  # 对列中元素的数量
print(queue.empty())  # 判断队列是否为空
