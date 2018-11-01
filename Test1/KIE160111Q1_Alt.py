a=str(input('Enter a five-digit number: '))
print('The digits in reverse order :',end="")
for i in range(len(a)):
    print((a)[::-1][i],end="\t")
print('\nAddition : ',(a)[::-1][0],'+',(a)[::-1][2],'+',(a)[::-1][4],'=',int((a)[::-1][0])+int((a)[::-1][2])+int((a)[::-1][4]))
print('Multiplication : ',(a)[::-1][1],'x',(a)[::-1][3],'=',int((a)[::-1][1])*int((a)[::-1][3]))