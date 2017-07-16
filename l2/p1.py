#citirea numarului
def citesteIntSecure():
    while True:
        try:
            n=int(input("Introduceti numarul: "))
            return n
        except ValueError:
            print("Am zis numar ! ")
#verificare ca un numar ii prim
def prim(n):
    pass
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
        d+=2
    return True
#gasirea nr prim superior numarului dat
def gaseste():
    n=citesteIntSecure()
    while prim(n)==False:
        n=n+1
    return n
print(gaseste())
assert prim(3)==True
assert prim(4)==False
assert prim(-1)==False

