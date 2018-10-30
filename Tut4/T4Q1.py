#Question 1(a)
x=[1,2,3]
y=x
x[1]=555
print("x,y: ",x,y)
#Question 1(b)
x=[1,2,3]
y=x[:] #y=x.copy()
x[1]=555
print("x,y: ",x,y)
