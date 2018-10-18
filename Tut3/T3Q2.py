print('*** Integer Input ***')

while 1:
   a=input('Please enter an integer: ')
   if a.isdigit():
       break
   print('Error!',end=' ')
print('Integer entered is ',a)      
print('*** End ***')