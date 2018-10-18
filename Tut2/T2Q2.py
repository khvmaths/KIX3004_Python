import math

print('***Quadratic Equation Solver***')
print('Please key in the following quadratic equation coefficients')
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))

coeff=b**2-4*a*c

print('The solutions for the quadratic equations are')
if coeff>0:
    x1=(-b+math.sqrt(coeff))/(2*a)
    x2=(-b-math.sqrt(coeff))/(2*a)
    print('x1 = %f\nx2 = %f' %(x1,x2))
elif coeff==0:
    x1=(-b+math.sqrt(coeff))/(2*a)
    x2=x1
    print('x1 = %f\nx2 = %f' %(x1,x2))
else:
    x1r=(-b/(2*a))
    x1i=((math.sqrt(-coeff))/(2*a))
    x2r=(-b/(2*a))
    x2i=((math.sqrt(-coeff))/(2*a))
    print('x1 = %f+%fj' %(x1r,x1i))
    print('x2 = %f-%fj' %(x2r,x2i))

print('*** End ***')