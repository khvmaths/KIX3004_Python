#KOAY HONG VIN KIE160111
v,c,r=[],[],[]
for _ in range(4):
    v.append(float(input('Enter the voltage : ')))
    c.append(float(input('Enter the current : ')))
    r.append(float(input('Enter the rpm : ')))
    
print('Voltage\tCurrent\tRPM\tRange')
for i in range(4):
    q=float((v[i]*1.2)+(c[i]*0.5)+(r[i]*0.2))
    print(v[i],c[i],v[i],q,sep="\t")