"""
属性的初始化：
都可以在方法内部，当方法被调用时初始化
"""


class Cat():
    col = "yello"

    def jump(self, name):
        self.cat_name = name  # 定义对象属性，且只能由对象访问得到
        Cat.name = "xiaohei"  # 定义类属性，类和对象都可以访问得到
        pass


if __name__ == "__main__":
    cat = Cat()
    cat.jump("xiaohua")
    print(cat.cat_name)
    print(Cat.name)
    pass
