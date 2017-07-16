'''
Created on Oct 29, 2016

@author: Ursu
'''
from utils import citireComanda
from controller import runAdauga,runCauta,runFiltrare,runModifica,runOperatii
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
    print("6.Undo (merge doar o data)")
    print("x.Iesire")
def meniuAdauga(l):
    print("a.Adauga un numar la sfarsit")
    print("b.Adauga un numar pe o pozitie")
    runAdauga(l)