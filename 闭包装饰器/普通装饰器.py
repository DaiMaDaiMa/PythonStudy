"""
首先要有闭包
@引用装饰器
"""


def function_out(func):
    def function_in():
        print("登录前先验证:")
        func()
    return function_in


@function_out
def login():
    print("登录")


login()
