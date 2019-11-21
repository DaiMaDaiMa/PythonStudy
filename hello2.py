#!/usr/bin/env python
x=1
def f1():
    x=2
    print("x",x)
    print(id(x))
    def f2():
        # x=3
        def f3():
        	        #global x#修改全局的
        	nonlocal x#修改局部的（当用nonlocal时，修改x=3为x=100000000，当x=3不存在时，修改x=2为100000000 ）
        	                 # 必须在函数内部
        	x=10000000000
        	print("f3内的打印x",x)
        	print(id(x))
        f3()
        print('f2内的打印',x)
        print(id(x))
    f2()
    print('f1内的打印', x)
    print(id(x))
f1()
print("全局x : ", x)
print(id(x))


"""
在函数内部使用nonlocal关键字，会可以修改整个函数内部的局部变量x。
但是修改后的局部变量将不再是最开始的那个局部变量。因为内存地址发生了改变
。局部变量的更改，不会影响到全局变量x

使用global关键字声明的对象，之前可以不存在，而nonlocal申明的对象，必须之前已经存在
"""

