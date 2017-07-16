#citire numar de la tastatura
def citire():
    while True:
        try:
            n=int(input("Introduceti nr: "))
            return n
        except ValueError:
            print("numar taticule...")
#verificare ca un nr este prim
def prim(p):
    if p<2:
        return False
    if p==2:
        return True
    if p%2==0:
        return False
    d=3
    while d*d<=p:
        if p%d==0:
            return False
        d+=2
    return True
#gasirea celor 2 numere...babeste
def FindNr():
    n=citire()
    for i in range(2,n):
        for j in range(2,n):
            if prim(i)&prim(j):
                if i+j==n:
                    return i,j
    return False
print(FindNr())

assert prim(23)
assert prim(2)
assert prim (1)==False
assert prim(-3)==False
assert prim(4)==False



            
