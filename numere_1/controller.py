'''
Created on Oct 29, 2016

@author: Ursu
'''
from validator import *
from utils import *
#l1 - lista de undo
l1=[]
def undo(l):
    try:
        del l1[len(l1)-1]
        del l[:]
        l.extend(l1[len(l1)-1])
    except IndexError:
        print("Imposibil de realizat Undo")
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
    l1=[]
    for i in range(st,dr+1):
        l1.append(l[i][1])
    return l1


def afiseazaModulMic(l):
    '''
    Afiseaza numerele din lista cu modulul <10
    date de intrare:
    l- lista de numere
    '''
    l1=[]
    for i in range(len(l1)):
        if modulNumar(l[i][0],l[i][1])<10:
            l1.append(l[i])
    return l1
def afiseazaModulEgal(l):
    '''
    Afiseaza numerele din lista cu modulul =10
    date de intrare:
    l - lista de numere
    '''
    l1=[]
    for i in range(len(l)):
        if modulNumar(l[i][0],l[i][1])==10:
            l1.append(l[i])
    return l1
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
    return s
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
    return p


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
