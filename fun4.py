# funkcja zagniezdzona
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # bez nawiasow


xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000001ABD3B4CE00>
xFun()  # To jest fun2
