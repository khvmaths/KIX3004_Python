f=open('dictionary.txt')
lines=f.readlines()
f.close()
for l in lines:
    if(len(l)==5 and l[0]=='a' and l[1]=='c' and l[2]=='h'):
        print(str(l))