"""
具体方法的实现
center（）
hello（）
gettime（）
"""
import time


def center():
    return "this is center"


def hello():
    return "this is hello"


def gettime():
    return "this is time %s" % time.ctime()
