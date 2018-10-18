S=input("Enter a string : ")
s=""
for i in range(1,len(S)+1):
    s+=S[len(S)-i]
print("The reversed of ",S," is ",s)
#print("The reversed of ",S," is ","".join(reversed(S)))