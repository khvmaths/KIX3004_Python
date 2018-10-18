list1,list2=[],[]
for i in range (25):
    list1.append(1)
while len(list2)<25:
    list2.append(1)
list3=[1]*25
list4=[1 for i in range(25)]
print(list1,list2,list3,list4,sep="\n")