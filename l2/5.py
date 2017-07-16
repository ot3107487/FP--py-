#citirea
def cit():
    while True:
        try:
            n=int(input("Baga n-u'"))
            return n
        except ValueError:
            print("Adica numarul")
#algoritmul de nr prim
def prim(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d=d+1
    return True
#gasirea perchei
def genereaza():
    n=cit()
    while True:
        if prim(n)&prim(n+2):
            return n,n+2
        n=n+1
print(genereaza())

assert prim(23)
assert prim(2)
assert prim (1)==False
assert prim(-3)==False
assert prim(4)==False



