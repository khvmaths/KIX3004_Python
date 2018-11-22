def sum_iter(n):
    t=0
    i=1
    while i<(2*n)+1:
        if i%2==1:
            t+=i
        i+=2
    return t

def sum_rec(n):
    if n==1:
        return 1
    else:
        return 2*n-1+sum_rec(n-1)
    
print(sum_iter(3))
print(sum_rec(3))