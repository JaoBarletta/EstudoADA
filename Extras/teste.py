def soma(a,b):
    print(2)
    return a + b

def soma2(a,b):
    print(3)
    return soma(a,b)


a,b = 1,2
print(soma2(a,b))