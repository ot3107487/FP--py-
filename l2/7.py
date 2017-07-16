#citeste pe n
def cit():
    while True:
        try:
            n=int(input("Introduceti numarul:"))
            return n
        except ValueError:
            print("Intreg daca se poate")
#calcularea produsului
def prod():
    n=cit()
    p=1
    for d in range(2,int(n/2)+1):
        if n%d==0:
            p=p*d
    if p==1:
        return -1
    return p
print (prod())
