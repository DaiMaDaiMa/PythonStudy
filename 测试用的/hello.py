#!/usr/bin/env python
x=1
def f1():
    x=2
    print(id(x))
    def f2():
        # x=3
        def f3():
	        global x#修改全局的
	            #nonlocal x#修改局部的（当用nonlocal时，修改x=3为x=100000000，当x=3不存在时，修改x=2为100000000 ）
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

得出结论。在哪个作用域中使用了global关键字，修改了全局变量x，那么全局变量x，也只仅仅在这个作用域中有效，跟其他作用域没有关系
若其他作用域也想修改全局变量x,也必须使用global关键字
"""

