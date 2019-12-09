
def function_out(num):
    def function_in():
        print("内部函数引用外部函数变量num", num)
    return function_in


if __name__ == "__main__":
    fc = function_out(10)
    fc()
