import cProfile

def f1():
    total = 0
    for var in range(100000):
        total += var
    return total

cProfile.run("f1()")