"""
1.class mylist 三个方法：构造方法，实例化一个列表；additems,添加数据；__iter()__，生成迭代器,__next__，根据下标返回数据
"""


class MyList():

    def __init__(self):

        self.list = []
        self.current_index = 0

    def additems(self, data):

        self.list.append(data)

    def __iter__(self):

        return self

    def __next__(self):
        if self.current_index < len(self.list):
            data = self.list[self.current_index]
            self.current_index += 1
            return data

        else:
            raise StopIteration


if __name__ == "__main__":
    mylist = MyList()
    mylist.additems("你好")
    mylist.additems("hello")
    mylist.additems("world")
    mylist.additems("python")
    for values in mylist:
        print(values)
