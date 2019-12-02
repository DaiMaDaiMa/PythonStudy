import multiprocessing
import time


def work():
    for i in range(10):
        print("子进程", i)
        time.sleep(0.5)


if __name__ == "__main__":
    mp = multiprocessing.Process(target=work)
    # mp.daemon = True  # 被动结束。子进程守护主进程，主进程结束了，子进程也要结束
    mp.start()

    time.sleep(2)
    print("主进程结束了")
    mp.terminate()  # 主动结束，子进程强制结束
    exit()
