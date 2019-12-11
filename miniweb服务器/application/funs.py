"""
具体方法的实现
center（）
hello（）
gettime（）
"""
import time
import sys
sys.path.append("miniweb服务器\application")

from application import urls


def route(path):
    def function_out(func):
        urls.route_dict[path] = func

        def function_in():
            return func()
        return function_in
    return function_out


@route("/center.py")
def center():
    return "this is center"


@route("/hello.py")
def hello():
    return "this is hello"


@route("/gettime.py")
def gettime():
    return "this is time %s" % time.ctime()
