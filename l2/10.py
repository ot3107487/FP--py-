#citire
def cit():
    while True:
        try:
            n=int(input("Introduceti nr: "))
            return n
        except ValueError:
            print("Numar..")
#scoaterea cifrelor lui n si construirea minimului
# lista c este lista de frecventa a cifrelor initializata cu 0
def cifre(n):
    c=[]
    rez=0
    for i in range(0,10):
        c.append(0)
    while n>0:
        c[n%10]=c[n%10]+1
        n=n//10
    i=1
    while i<10:
        if c[i]>0:
            rez=i
            c[i]=c[i]-1
            break
        i=i+1
    for i in range(0,10):
        for j in range(1,c[i]+1):
            rez=rez*10+i
    return rez
print(cifre(cit()))

assert cifre(425)==245

        
