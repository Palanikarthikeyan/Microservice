import cProfile


def f1():
    total = 0
    for var in range(5000000):
        total = total + var
    return total

def f2():
    total = 0
    for var in range(1000000000):
        total = total+var
    return total

def f3():
    f1()
    f2()
    
cProfile.run("f3()","profile_results.pdf")
