# KOAY HONG VIN (KIE160111)

a=int(input('Enter a five-digit number: '))
num=[]
for i in range(5):
    num.append(int(a/(10**i)%10))
print('The digits in reverse order:',end="")
for i in range(5):
    print(num[i],end="\t")
print('',end='\n')
print('Addition : ',num[0],'+',num[2],'+',num[4],'=',num[0]+num[2]+num[4])
print('Multiplication : ',num[1],'x',num[3],'=',num[1]*num[3])