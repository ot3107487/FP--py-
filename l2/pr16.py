def cit():
    while True:
            try:
                n=int(input("introduceti numarul:"))
                return n
            except ValueError:
                print("Intreg/numar")
def sumadiv(n):
    s=0
    for d in range(1,int(n/2)+1):
        if n%d==0:
            s+=d
    return s
def gasestenr(n):
    while n>=4:
        if n==sumadiv(n):
            return n
        n=n-1
    return 0
def conditie(n):
    if n>0:
        print (n)
    else:
        print ("Nu exista")
conditie(gasestenr(cit()))
assert sumadiv(2)==1
assert sumadiv(6)==6
assert sumadiv(10)==8

            
