"""
  通过对象和类分别访问私有方法
   但类无法访问对象的属性，无论是公有还是私有
   
"""


class Person():
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s 的年龄是 %d" % (self.name, self.__age))


if __name__ == "__main__":
    p = Person("xiaofang")
    print(p._Person__age)
    p._Person__secret()
    Person._Person__secret(p)
