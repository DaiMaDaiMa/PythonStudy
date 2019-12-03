"""
1.class mylist 三个方法：构造方法，实例化一个列表；additems,添加数据；__iter()__，生成迭代器
2.class mylistiterator 三个方法：构造方法，接收mylist对象的列表，实例化下标属性；__item__,返回迭代器；__next__，根据下标返回数据
"""


class MyList():

    def __init__(self):

        self.list = []

    def additems(self, data):

        self.list.append(data)

    def __iter__(self):
        mylist_iterator = MylistIterator(self.list)

        return mylist_iterator


class MylistIterator():

    def __init__(self, list):
        self.list = list

        self.current_index = 0

    # def __iter__(self):
    #     pass

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
