'''
Created on Oct 29, 2016

@author: Ursu
'''
from utils import *
from validator import validPoz,validPozitii
def adaugaSfarsit(l,real,imag):
    '''
    Adauga un numar complex la sfarsitul listei
    date de intrarE:
    l - lista de numere complexe
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
    validPoz(l,poz)
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
    validPoz(l,poz)
    del l[poz]
def stergePozitii(l,st,dr):
    '''
    Sterge elementele cu indicii in [st,dr]
    date de intrarE:
    l - lista de numere
    st - inceputul intervalului
    dr - sfarsitul intervalului
    '''
    validPozitii(l,st,dr)
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
    validPozitii(l,st,dr)
    for i in range(st,dr+1):
        print(l[i][1])


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
    validPozitii(l, st, dr)
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
    validPozitii(l,st,dr)
    p=[1,0]
    for i in range(st,dr+1):
        real=p[0]*l[i][0]-p[1]*l[i][1]
        imag=p[1]*l[i][0]+p[0]*l[i][1]
        p[0]=real
        p[1]=imag
    print(p)


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


