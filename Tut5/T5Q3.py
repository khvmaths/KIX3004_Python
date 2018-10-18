from functools import reduce

def f(a,b):
    return a+b 

a=[1,-2,5,6,8]
t=reduce(f,filter(lambda a: a>0,a))
print(t)