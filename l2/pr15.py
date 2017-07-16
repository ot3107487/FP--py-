# functie de citire si validare ca ai introdus un NR
def citesteIntSecure():
    while True:
        try:
            n=int(input("Introduceti nr:"))
            return n
        except ValueError:
            print("Introduceti un numar")
#verificare ca un numar este prim
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
#gasirea numarului prima mai mic decat numarul
def numar(n):
    while n>=2:
        if prim(n):
            return n
        n=n-1
    return -1
#afisarea rezultatului final
def afiseaza(n):
    i=numar(n)
    if i>0:
        print(i)
    else:
        print("Nu exista")

afiseaza(citesteIntSecure())
assert prim(2)==True
assert prim(4)==False
assert prim(15)==False
assert prim(0)==False
assert prim(-1)==False
assert prim(23)


        
        
