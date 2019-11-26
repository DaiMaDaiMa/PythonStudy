import weakref
from sys import getrefcount


class Test():
    pass


if __name__ == "__main__":

    test = Test()
    weak = weakref.proxy(test)
    print(test)
    print(weak)
    print(getrefcount(test))
    del test
    try:
        weak.__name__
        print(weak)
    except ReferenceError:
        print("None")
