"""
以字典的形式，保存路径和对应的方法名
"""
from application import funs

route_dict = {

    "/center.py": funs.center,
    "/hello.py": funs.hello,
    "/gettime.py": funs.gettime,

}
