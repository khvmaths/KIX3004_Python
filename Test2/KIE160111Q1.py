from functools import reduce

A=[1,-2,3.5+4j,4.5,5,4-3.5j,3.5,3,-5.5]

#Question 1
floating=list(filter(lambda x:x if x.imag==0 and type(x)==float else 0,A))
print(floating)

#Question 2
comp=list(filter(lambda x:x if x.imag!=0 else 0,A))
print(comp)

#Question 3
sum_non=reduce(lambda x,y:x+y,filter(lambda x: x if type(x)==int and x>=0 else 0,A))
print(sum_non)

#Question 4
sum_mag=reduce(lambda x,y:x+y,map(lambda a:(a.real**2+a.imag**2)**0.5 if type(a)==complex else a,A))
print(sum_mag)

#Question 5
maxi=reduce(lambda x,y: x if x>y else y, map(lambda a:(a.real**2+a.imag**2)**0.5 if type(a)==complex else a,A))
print(maxi)
mini=reduce(lambda x,y: y if x>y else y, map(lambda a:(a.real**2+a.imag**2)**0.5 if type(a)==complex else a,A))
print(mini)