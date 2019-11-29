import threading


a = "hello"
b = 10


def f1():
    global a
    a = a+"hello"
    print(a)


def f2():

    print(a)


def f3():
    global b
    b = b + 10  # 访问外部变量，可以直接访问打印，但不能运算。。UnboundLocalError
    print("f3", b)


def f4():
    # global b
    print("f4", b)


if __name__ == "__main__":
    # f1()
    # f2()
    # f3()
    # f4()
    tf3 = threading.Thread(target=f3)
    tf4 = threading.Thread(target=f4)
    tf3.start()
    tf4.start()


"""
在一个方法中，申明变量为全局变量，其他方法也可以访问得到，并且可以得到被修改后的值

在一个进程中，global申明的全局变量，在线程间也是共享的
"""
