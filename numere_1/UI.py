'''
Created on Oct 29, 2016

@author: Ursu
'''
from controller import *

def citesteIntSecure(mesaj):
    while True:
        try:
            n=int(input(mesaj))
            return n
        except ValueError:
            print("Introduceti o valoare numerica intreaga")
def citireComanda():
    return input("Introduceti comanda: ")
def afisareLista(l):
    print("Remember the list:")
    print(l)
def meniuFiltrare(l):
    print("a.Filtrare parte reala prim - elimina numere cu partea reala prima")
    print("b.Filtrare modul - elimina din lista nr cu modulul <,> sau = cu un numar dat")
    runFiltrare(l)
def meniuOperatii(l):
    print("a.Suma numerelor dintr-o subsecventa data")
    print("b.Produsul numerelor dintr-o subsecventa data")
    print("c.Tipreste lista sortata descrescator dupa partea imaginara")
    runOperatii(l)
def meniuCauta(l):
    print("a.Afizeaza partea imaginara a numerelor situate pe pozitii din interval")
    print("b.Afiseaza toate numerel cu modulul < 10")
    print("c.Afiseaza toate numerele cu modulul = 10")
    runCauta(l)
def meniuModifica(l):
    print("a.Sterge un numar de pe o pozitie")
    print("b.Sterge numerele de pe un interval de pozitii")
    print("c.Inlcuieste un numar cu altul")
    runModifica(l)
def meniu():
    print("1.Adauga numar in lista")
    print("2.Modifica elemente din lista")
    print("3.Cautare numere")
    print("4.Operatii cu numerele din lista")
    print("5.Filtrare")
    print("6.Undo")
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
                print(cauta[cmd](l,st,dr))
            except ValueError as ex:
                print(ex)
        if cmd=="b":
            try:
                print(cauta[cmd](l))
            except ValueError as ex:
                print(ex)
        if cmd=="c":
            try:
                print(cauta[cmd](l))
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
                print(operatii[cmd](l,st,dr))
            except ValueError as ex:
                print(ex)
        if cmd=="b":
            st=citesteIntSecure("Introduceti inceputul secventei: ")
            dr=citesteIntSecure("Introduceti sfarsitul secventei: ")
            try:
                print(operatii[cmd](l,st,dr))
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
def meniuUndo(l):
    undo(l)
