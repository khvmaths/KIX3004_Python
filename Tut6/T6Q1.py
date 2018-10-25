def fibo_generator():
    a,b=0,1
    while 1:
        yield a
        a,b=b,a+b

fibo_generator_object = fibo_generator()

print(next(fibo_generator_object))
print(next(fibo_generator_object))

for _ in range (50) :
    print(next(fibo_generator_object), end=', ')
