#citeste nr - merge pe premiza ca ultima cifra este diferita de 0
#nu stiu sa pun in try treaba asta.
def cit():
    while True:
        try:
            n=int(input("Numarul esteee:"))
            return n
        except ValueError:
            print("Un numar cu ultima cifra diferita de 0")
#construirea palidromului
def pal(n):
    d=0
    c=0
    while n>0:
        c=n%10
        d=d*10+c
        n=n//10
    return d
print(pal(cit()))
assert pal(223)==322




    
