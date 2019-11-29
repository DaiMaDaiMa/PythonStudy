import threading


def get_data(index):
    data_list = [2, 3, 45, 6, 8]
    lock.acquire()

    if index >= len(data_list):
        print("角标越界，", index)
        lock.release()  # 在return之前，，将锁释放，可以避免死锁
        return

    print("打印值：", data_list[index])
    lock.release()


if __name__ == "__main__":

    lock = threading.Lock()
    for i in range(10):
        t = threading.Thread(target=get_data, args=(i, ))
        t.start()
