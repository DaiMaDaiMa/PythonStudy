class Dog():
    name = "hashiqi"
    pass

if __name__ == "__main__":
    dog = Dog()
    dog.name = "maomao"
    print(dog.name)   # 这里dog对象，只是定义了一个对象属性而已，而名字恰巧相同
    Dog.name = "zangao"   # 这里Dog类，修改了类属性
    print(Dog.name+"类  ")
    pass