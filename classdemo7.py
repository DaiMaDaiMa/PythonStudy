class Person():
    age = 18
    __tall = 1.75
    def ___init__(self, name):

        pass

    def say(self):
        print("父类说")
        Person.___cry(self)
        pass

    def ___cry(self):
        print("父类哭")
        pass


class zhangsan(Person):
    def __init__(self, name):
        pass

    pass


if __name__ == "__main__":
    zs = zhangsan("xiaowang")
    zs.say()  # 子类对象访问父类方法
    print(zs.age)  # 子类对象访问父类属性
    # print( zs._Person__tall)  # 子类对象访问父类私有属性
    # print(dir(zs))
    # zs._Person__cry()  # 好像无法正常访问父类私有方法
