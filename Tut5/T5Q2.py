from functools import reduce

def g(m,n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum

n=5
f=reduce(g,range(n+1) if n>0 else range (n+2))
print(f)
