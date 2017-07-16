def citesteIntSecure(mesaj):
    while True:
        try:
            n=int(input(mesaj))
            return n
        except ValueError:
            print("Introduceti o valoare numerica intreaga")
def adaugaSfarsit(l,real,imag):
    '''
    Adauga un numar complex la sfarsitul listei
    date de intrarE:
x    l - lista de numere complexe
    real - partea reala a nr
    imag - partea imaginara a nr
    date de iesire:
    l- lista modificata
    '''
    l.append([real,imag])
def adaugaPozitie(l,real,imag,poz):
    '''
    Adauga un numar pe o pozitie data
    date de intrare:
    l - lista de numere
    real - partea reala a numarului
    imag - partea imaginara a numarului
    poz - pozitia
    date de iesire:
    l - lista modificata
    '''
    if poz>len(l):
        raise ValueError("Nu exista acea pozitie")
    l.append(0)
    for i in range(len(l)-1,poz,-1):
        l[i]=l[i-1]
    l[poz]=[real,imag]
def stergePoz(l,poz):
    '''
    Sterge elemntul de pe pozitia poz din lista l
    date de intrare:
    l- lista de numere
    poz - pozitia
    date de iesire:
    l - lista modificata
    '''
    if poz>len(l):
        raise ValueError("Nu exista acea pozitie")
    del l[poz]
def stergePozitii(l,st,dr):
    '''
    Sterge elementele cu indicii in [st,dr]
    date de intrarE:
    l - lista de numere
    st - inceputul intervalului
    dr - sfarsitul intervalului
    '''
    if st>dr and dr>len(l):
        raise ValueError("Interval incorect")
    for i in range(st,dr+1):
        del l[st]
def inlocuireNumar(l,nr1,nr2):
    '''
    Inlocuieste numarul nr1 din lista cu nr 2
    date de intrare:
    l - lista de numere
    nr1- numarul de inlocuit
    nr2 - numarul cu care se inlocuieste nr1
    date de iesire:
    l -lista modificata
    '''
    for i in range(len(l)):
        if l[i]==nr1:
            l[i]=nr2
    
def afiseazaPIPozitii(l,st,dr):
    '''
    Afiseaza partea imaginara a numerelor cu indicii in [st,dr]
    date de intrarE:
    l - lista de numere
    st - capatul din stanga al intervalului
    dr - capatul din dreapta al intervalului
    '''
    if st>dr and dr>len(l):
        raise ValueError("Interval incorect")
    for i in range(st,dr+1):
        print(l[i][1])
def modulNumar(real,imag):
    '''
    Returneaza modulul unui numar complex
    date de intrare:
    real - partea reala a numarului
    imag - partea imaginara a numarului
    date de iesire:
    modulul numarului
    '''
    return sqrt(real*real+imag*imag)
def testModulNumar():
    assert modulNumar(1,1)==sqrt(2)
def afiseazaModulMic(l):
    '''
    Afiseaza numerele din lista cu modulul <10
    date de intrare:
    l- lista de numere
    '''
    for i in range(len(l)):
        if modulNumar(l[i][0],l[i][1])<10:
            print(l[i])
def afiseazaModulEgal(l):
    '''
    Afiseaza numerele din lista cu modulul =10
    date de intrare:
    l - lista de numere
    '''
    for i in range(len(l)):
        if modulNumar(l[i][0],l[i][1])==10:
            print(l[i])
def sumaNumereSecventa(l,st,dr):
    '''
    Afiseaza suma numerelor complexe cu indicii in [st,dr]
    date de intrare:
    l - lista de numere
    st - capatul din stanga
    dr - capatul din dreapta
    '''
    if st>dr and dr>len(l):
        raise ValueError("Interval incorect")
    s=[0,0]
    for i in range(st,dr+1):
        s[0]+=l[i][0]
        s[1]+=l[i][1]
    print(s)
def produsNumereSecventa(l,st,dr):
    '''
    Afiseaza produsul numerelor compexe cu indicii in [st,dr]
    date de intrare:
    l- lista de numere
    st - capatul din stanga
    dr - capatul din dreapta
    '''
    if st>dr and dr>len(l):
        raise ValueError("Interval incorect")
    p=[1,0]
    for i in range(st,dr+1):
        real=p[0]*l[i][0]-p[1]*l[i][1]
        imag=p[1]*l[i][0]+p[0]*l[i][1]
        p[0]=real
        p[1]=imag
    print(p)
def sortareLista(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i][1]<l[j][1]:
                aux=l[i]
                l[i]=l[j]
                l[j]=aux
def prim(n):
    '''
    Functia care verifica dace un numar e prim ..
    '''
    if n==2:
        return True
    if n<2:
        return False
    if n%2==0:
        return False
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True
def parteRealaPrima(l):
    '''
    Functia sterge numerele din lista care au partea reala prima
    date de intrare:
    l - lista de numere
    date de iesire:
    l - lista modificata
    '''
    i=0
    while i<len(l):
        if prim(l[i][0]):
            del l[i]
        else:
            i+=1
def maiMic(a,b):
    if a<b:
        return True
    return False
def maiMare(a,b):
    if a>b:
        return True
    return False
def egal(a,b):
    if a==b:
        return True
    return False
def eliminaModul(l,k,functie):
    '''
    Functia elimina numerele cu modulul <,> sau = cu k
    date de intrare:
    l - lista de numere
    k - numarul de referinta
    functie - o procedura data ca parametru ca sa nu fac 3 functii pt fiecare caz
    date de iesire:
    l - lista modificcata
    '''
    i=0
    while i<len(l):
        a=modulNumar(l[i][0],l[i][1])
        if functie(a,k):
            del l[i]
        else:
            i+=1
def testPrim():
    assert prim(2)
    assert prim(4)==False
    assert prim(0)==False
    assert prim(-1)==False
    assert prim(20)==False
def testAdaugaSfarsit():
    l=[]
    adaugaSfarsit(l,1,2)
    assert l==[[1,2]]
    adaugaSfarsit(l,3,4)
    assert l==[[1,2],[3,4]]
def teste():
    l=[[1,2],[3,4],[5,6],[6,8]]
    testAdaugaSfarsit()
    #afiseazaPIPozitii(l,1,3)
    #afiseazaModulMic(l)
    #afiseazaModulEgal(l)
    testModulNumar()
    parteRealaPrima(l)
    assert l==[[1,2],[6,8]]
    testPrim()
    testUndo()
def conditieUndo(l1,l):
    '''
    Verifica daca lista l  este deja in lista l1
    '''
    if len(l1)>0 and l1[len(l1)-1]==l:
        return False
    return True
def testUndo():
    l1=[[[1,2],[3,4]],[[2,3],[5,6]]]
    l=[[2,3],[5,6]]
    assert conditieUndo(l1,l)==False
    l=[[1,0],[3,4]]
    assert conditieUndo(l1,l)
def meniu():
    print("1.Adauga numar in lista")
    print("2.Modifica elemente din lista")
    print("3.Cautare numere")
    print("4.Operatii cu numerele din lista")
    print("5.Filtrare")
    print("6.Undo (merge doar o data)")
    print("x.Iesire")
def meniuAdauga(l):
    print("a.Adauga un numar la sfarsit")
    print("b.Adauga un numar pe o pozitie")
    runAdauga(l)
def runAdauga(l):
    adauga={"a":adaugaSfarsit,"b":adaugaPozitie}
    cmd=citireComanda()
    if cmd in adauga:
        real=citesteIntSecure("Introduceti partea reala: ")
        imag=citesteIntSecure("Introduceti partea imaginara: ")
        if cmd=="a":
            try:
                adauga[cmd](l,real,imag)
            except ValueError as ex:
                print(ex)
        if cmd=="b":
            poz=citesteIntSecure("Pozitia pe care vreti sa adaugati: ")
            try:
                adauga[cmd](l,real,imag,poz)
            except ValueError as ex:
                print(ex)
    else:
        print("Command error! Inserts sth else")
def meniuModifica(l):
    print("a.Sterge un numar de pe o pozitie")
    print("b.Sterge numerele de pe un interval de pozitii")
    print("c.Inlcuieste un numar cu altul")
    runModifica(l)
def runModifica(l):
    modifica={"a":stergePoz,"b":stergePozitii,"c":inlocuireNumar}
    cmd=citireComanda()
    if cmd in modifica:
        if cmd=="a":
            poz=citesteIntSecure("Introduceti pozitia: ")
            try:
                modifica[cmd](l,poz)
            except ValueError as ex:
                print(ex)
        if cmd=="b":
            st=citesteIntSecure("Inceputul intervalului: ")
            dr=citesteIntSecure("Sfarsitul intervalului: ")
            try:
                modifica[cmd](l,st,dr)
            except ValueError as ex:
                print(ex)
        if cmd=="c":
            real1=citesteIntSecure("PR a nr-ului de inlocuit: ")
            imag1=citesteIntSecure("PI a nr-ului de inlocuit: ")
            real2=citesteIntSecure("PR a nr-ului cu care se inlocuieste: ")
            imag2=citesteIntSecure("PI a nr-ului cu care se inlocuieste: ")
            try:
                modifica[cmd](l,[real1,imag1],[real2,imag2])
            except ValueError as ex:
                print(ex)
    else:
        print("Command error! Inserts sth else")
def meniuCauta(l):
    print("a.Afizeaza partea imaginara a numerelor situate pe pozitii din interval")
    print("b.Afiseaza toate numerel cu modulul < 10")
    print("c.Afiseaza toate numerele cu modulul = 10")
    runCauta(l)
def runCauta(l):
    cauta={"a":afiseazaPIPozitii,"b":afiseazaModulMic,"c":afiseazaModulEgal}
    cmd=citireComanda()
    if cmd in cauta:
        if cmd=="a":
            st=citesteIntSecure("Inceputul intervalului: ")
            dr=citesteIntSecure("Sfarsitul intervalului: ")
            try:
                cauta[cmd](l,st,dr)
            except ValueError as ex:
                print(ex)
        if cmd=="b":
            try:
                cauta[cmd](l)
            except ValueError as ex:
                print(ex)
        if cmd=="c":
            try:
                cauta[cmd](l)
            except ValueError as ex:
                print(ex)
    else:
        print("Command error! Inserts sth else")
def meniuOperatii(l):
    print("a.Suma numerelor dintr-o subsecventa data")
    print("b.Produsul numerelor dintr-o subsecventa data")
    print("c.Tipreste lista sortata descrescator dupa partea imaginara")
    runOperatii(l)
def runOperatii(l):
    operatii={"a":sumaNumereSecventa,"b":produsNumereSecventa,"c":sortareLista}
    cmd=citireComanda()
    if cmd in operatii:
        if cmd=="a":
            st=citesteIntSecure("Introduceti inceputul secventei: ")
            dr=citesteIntSecure("Introduceti sfarsitul secventei: ")
            try:
                operatii[cmd](l,st,dr)
            except ValueError as ex:
                print(ex)
        if cmd=="b":
            st=citesteIntSecure("Introduceti inceputul secventei: ")
            dr=citesteIntSecure("Introduceti sfarsitul secventei: ")
            try:
                operatii[cmd](l,st,dr)
            except ValueError as ex:
                print(ex)
        if cmd=="c":
            try:
                operatii[cmd](l)
            except ValueError as ex:
                print(ex)
    else:
        print("Invali command! Try sth else")
def meniuFiltrare(l):
    print("a.Filtrare parte reala prim - elimina numere cu partea reala prima")
    print("b.Filtrare modul - elimina din lista nr cu modulul <,> sau = cu un numar dat")
    runFiltrare(l)
def runFiltrare(l):
    filtre={"a":parteRealaPrima,"b":meniuModul}
    cmd=citireComanda()
    if cmd in filtre:
        try:
            filtre[cmd](l)
        except ValueError as ex:
            print(ex)
    else:
        print("Comanda invalitda! Reintroduceti")
def meniuModul(l):
    print("i. Modul <k")
    print("ii. Modul =k")
    print("iii. Modul >k")
    runModul(l)
def runModul(l):
    module={"i":eliminaModul,"ii":eliminaModul,"iii":eliminaModul}
    cmd=citireComanda()
    if cmd in module:
        k=citesteIntSecure("Introduceti numarul de comparat: ")
        if cmd=="i":
            try:
                module[cmd](l,k,maiMic)
            except ValueError as ex:
                print(ex)
        if cmd=="ii":
            try:
                module[cmd](l,k,egal)
            except ValueError as ex:
                print(ex)
        if cmd=="iii":
            try:
                module[cmd](l,k,maiMare)
            except ValueError as ex:
                print(ex)
    else:
        print("Comanda invalida! Reintroduceti. ")
def citireComanda():
    return input("Introduceti comanda: ")
def afisareLista(l):
    print("Remember the list:")
    print(l)
def undo(l):
    try:
        del l1[len(l1)-1]
        del l[:]
        l.extend(l1[len(l1)-1])
    except IndexError:
        print("Imposibil de realizat Undo")
def run():
    l=[]
    categorii={"1":meniuAdauga,"2":meniuModifica,"3":meniuCauta,"4":meniuOperatii,"5":meniuFiltrare,"6":undo}
    while True:
        if conditieUndo(l1,l)==True:
            l1.append(list(l))
        meniu()
        afisareLista(l)
        cmd=citireComanda()
        if cmd=="x":
            return
        if cmd in categorii:
            try:
                categorii[cmd](l)
            except ValueError as ex:
                print(ex)            
        else:
            print("Command error! Insert sth else")
    
def main():
    teste()
    run()
from math import sqrt
from copy import deepcopy
l1=[]
main()
