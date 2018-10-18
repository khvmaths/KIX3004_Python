import math

print('Area Calculator for Basic Shapes')
print('================================',end='\n\n\n\t')
print('1. Square','2. Rectangle','3. Triangle','4. Circle',sep='\n\t')
a=int(input('Choose a shape [1-4] that you want calculate its area : '))
if a==1:
    l=float(input('Enter length : '))
    b=float(input('Enter base   : '))
    ans=l*b
    print('Area of square is %f' %ans)
elif a==2:
    l=float(input('Enter length : '))
    b=float(input('Enter base   : '))
    ans=l*b
    print('Area of rectangle is %f' %ans)
elif a==3:
    l=float(input('Enter length : '))
    b=float(input('Enter base   : '))
    ans=0.5*l*b
    print('Area of triangle is %f' %ans)
elif a==4:
    r=float(input('Enter radius : '))
    ans=math.pi*r*r
    print('Area of circle is %f' %ans)
else:
    print('Error!')
