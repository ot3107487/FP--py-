#citire numere
def cit():
    while True:
        try:
            n=int(input("Primul nr: "))
            m=int(input("Al doilea nr:"))
            return n,m
        except ValueError:
            print("numere")
#frecventa cifre n si m , a pentru n , b pentru m (liste)
def cifre(n,m):
    a=[]
    b=[]
    for i in range(0,10):
        a.append(0)
        b.append(0)
    while n>0:
        a[n%10]=a[n%10]+1
        n=n//10
    while m>0:
        b[m%10]=b[m%10]+1
        m=m//10
    print ("a=",a,"b=",b)
    for i in range (0,10):
        if a[i]>0 and b[i]==0 or a[i]==0 and b[i]>0:
            return False

    return True
i,j=cit()
print(cifre(i,j))


    
        
