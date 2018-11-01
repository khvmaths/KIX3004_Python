from functools import reduce

a=[10,30,20]
m=reduce(lambda x,y: x if x>y else y, a )
print(m)
