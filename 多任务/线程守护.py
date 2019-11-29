"""
当主线程结束的时候，设置子线程也结束
"""
import time
import threading


def sing():
    for i in range(10):
        print("我在唱歌。。。")
        time.sleep(0.5)


if __name__ == "__main__":
    thread_sing = threading.Thread(target=sing)
    thread_sing.setDaemon(True)
    thread_sing.start()
    time.sleep(2)
    exit()
