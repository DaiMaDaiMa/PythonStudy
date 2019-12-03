"""
生成器也是一样迭代器，可以使用next获取值
两种方式：
1.列表推导式
2.函数中使用了yield yield两个作用：1，充当return作用，2.保存程序状态
"""

data = (x for x in range(10))
print(data)
print(next(data))


def get_num():
    yield 10


num = get_num()
print(num)
print(next(num))
