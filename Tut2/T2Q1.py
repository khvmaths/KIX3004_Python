from numpy import arctan
import math

print('***Complex Number in Polar Form ***')
a=complex(input('Please enter a complex number: '))
m=(a.real**2+a.imag**2)**0.5
if a.real>0:
    p=arctan(a.imag/a.real)
else:
    p=arctan(a.imag/a.real)+math.pi
print('The complex number in polar form ')
print('m = %f\np = %f' %(m,p))
print('*** End ***')
