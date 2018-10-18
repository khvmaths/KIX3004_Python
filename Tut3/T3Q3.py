import math

marks=(35,40,50,60,80,88,20,40,75,99)
miu=sum(marks)/len(marks)

a,b,c,d,xmiu=0,0,0,0,0
for i in range(0,len(marks)):
    if marks[i]>=80:
        a=a+1
    elif marks[i]>=60:
        b=b+1
    elif marks[i]>=50:
        c=c+1
    else:
        d=d+1
    xmiu=xmiu+(marks[i]-miu)**2

print('*** Analysis of Student Marks ***')
print('A : %i\nB : %i\nC : %i\nD : %i' %(a,b,c,d))
print('Average = %.1f' %miu)
print('Varience = %.2f' %(xmiu/len(marks)))
print('Standard Deviation = %.2f' %(math.sqrt(xmiu/len(marks))))
print('*** End ***')