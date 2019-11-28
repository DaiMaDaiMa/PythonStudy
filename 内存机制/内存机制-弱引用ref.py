import weakref
class Test():
    pass


if __name__ == "__main__":
    
    test = Test()
    weak = weakref.ref(test)
    print(test)
    print(weak)
    del test
    print(weak())
    
    pass