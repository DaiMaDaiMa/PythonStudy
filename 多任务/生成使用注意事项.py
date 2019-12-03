"""
1、创建一个生成器
    目标：实现斐波那契数列
    1） 定义变量保存第一列和第二列的值
    2） 定义变量保存当前生成的位置

    3） 循环生成数据，条件（当前的列数 < 总列数）
    4） 保存 a 的值
    5） 修改 a \ b 的值  （a = b, b = a+b）
    6)  当前列数 + 1
    7)  返回 a 的值 yield

2、定义变量保存生成器
next(生成器） 得到下一个元素值


"""


# 1、创建一个生成器
def fibnacci(n):
    #     目标：实现斐波那契数列
    #     1） 定义变量保存第一列和第二列的值
    a = 1
    b = 1
    #     2） 定义变量保存当前生成的位置
    current_index = 0
    print("------1111111----------")
    #     3） 循环生成数据，条件（当前的列数 < 总列数）
    while current_index < n:
        #     4） 保存 a 的值
        data = a
        #     5） 修改 a \ b 的值  （a = b, b = a+b）
        a, b = b, a + b
        # 列数 +1
        current_index += 1
        #     6)  返回 a 的值 yield
        # 1, 充当return 作用
        # 2, 保存程序的运行状态 并且暂停程序执行
        # 3, 当next 的时候，可以继续唤醒程序从yield位置继续向下执行
        print("---------22222-------")
        xxx = yield data
        print("收到参数:", xxx)
        print("---------33333-------")

        if xxx == 1:
            # 生成器中能使用return 让生成器结束
            return "哈哈，我是return !我能让生成器结束!"


if __name__ == '__main__':

    # 2、定义变量保存生成器
    fib = fibnacci(5)
    # next(生成器） 得到下一个元素值

    value = next(fib)
    print("第1列", value)

    try:
        value = next(fib)
        print("第2列", value)

        value = fib.send(1)
        print("第3列", value)
    except Exception as e:
        print(e)
