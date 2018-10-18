from functools import reduce

def f(x,y):
    return x if x>y else y

a=[10,30,20]
m=reduce(f,a)
print(m)