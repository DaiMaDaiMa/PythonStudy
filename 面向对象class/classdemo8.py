"""单例模式
"""


class single(object):
    issingle = None
    isfirstinit = False

    def __new__(cls):
        if not single.issingle:
            cls.issingle = object.__new__(cls)
            #  single.issingle = True
        return cls.issingle

    def __init__(self):
        if not single.isfirstinit:
            print("第一次一定会被初始化，然后就不会再初始化了")
        single.isfirstinit = True

if __name__ == "__main__":
         # 调试的时候，不能在这里创建对象
        s1 = single()
        s2 = single()
        print(id(s1))
        print(id(s2))
        pass


# s1 = single()
# s2 = single()
# print(id(s1))
# print(id(s2))
