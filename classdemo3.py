class Fish():
    def size(self, color):
        self.color = color
        pass


if __name__ == "__main__":
    fish = Fish()
    fish.color = "red"
    print(fish.color)
    fish.color = "blue"  # 修改对象属性，由红变蓝
    print(fish.color)
    fish.eyes = "two"  # 动态的添加对象属性 eyes
    print(fish.eyes)
