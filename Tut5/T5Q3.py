from functools import reduce

a=[1,-2,5,6,8]
t=reduce(lambda x,y: x+y, filter(lambda a:a>0,a))
print(t)
