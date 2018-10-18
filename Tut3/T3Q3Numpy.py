import numpy as np

marks=np.array([35,40,50,60,80,88,20,40,75,99])

a,b,c,d=0,0,0,0
for i in range(0,len(marks)):
    a=a+1 if (marks[i]>=80) else a
    b=b+1 if (marks[i]>=60 and marks[i]<=79) else b
    c=c+1 if (marks[i]>=50 and marks[i]<=59) else c
    d=d+1 if (marks[i]<=49) else d
print('*** Analysis of Student Marks ***')
print('A : %i\nB : %i\nC : %i\nD : %i' %(a,b,c,d))
print('Average = %.1f' %np.average(marks))
print('Varience = %.2f' %np.var(marks))
print('Standard Deviation = %.2f' %np.std(marks))
print('*** End ***')