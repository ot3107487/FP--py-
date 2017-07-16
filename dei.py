def dei(l):
    if len(l)==1:
        if l[0]<=0:
            return l[0]
        else:
            return 1
    m=len(l)//2
    aux1=dei(l[:m])
    aux2=dei(l[m:])
    return aux1*aux2 
#print(dei([0,0,-2,0,-4]))
def dei2(l):
    if len(l)==1:
        if l[0]%2==0:
            return l[0]
        else:
            return 1
    m=len(l)//2
    aux1=dei2(l[:m])
    aux2=dei2(l[m:])
    return m
#print(dei2([2,3,4,5,6]))
def dei3(x,p,q,l):
    '''
trebuie sa gasesc unde pot sa inserez pe x intr-o lista ordonata.
'''
    m=(p+q)//2
    if p>q:
        return m+1
    m=(p+q)//2
    if l[m]==x:
        return m
    if l[m]>x:
        return dei3(x,p,m-1,l)
    if l[m]<x:
        return dei3(x,m+1,q,l)
print(dei3(5,0,6,[2,3,4,6,7,9,10]))
