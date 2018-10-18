from functools import reduce

c=[3+4j,5,5j]
m=reduce(lambda a,b:a+b,map(lambda a:(a.real**2+a.imag**2)**0.5,c))
print(m)