class Method():

    @classmethod
    def Cls_Method(cls):
        print("谁可以访问我")
        print(cls)
        pass


if __name__ == "__main__":

    m = Method()
    m.Cls_Method()
    Method.Cls_Method()  # 对象和类都可以访问类方法，而且默认传入的第一个方法都是类
    pass
