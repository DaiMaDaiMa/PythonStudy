class Person():

    def __del__(self):
        print("父类的删除方法")
    pass


class Xiao(Person):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        super().__del__() 
        # 最后需要说明的是，如果父类提供了 __del__() 方法，
        # 则系统重写 __del__() 方法时必须显式调用父类的 __del__() 方法，
        # 这样才能保证合理地回收父类实例的部分属性。
        # 因为子类继承父类，会继承父类所有的方法和属性，所以要先调用父类的del方法
        print("对象被删除了")


if __name__ == "__main__":
    xiao = Xiao("xiaoming")
    print(xiao.name)
    pass
