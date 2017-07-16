'''
Created on Oct 29, 2016

@author: Ursu
'''
from utils import modulNumar,prim,sortareLista
from validator import validPoz
from math import sqrt
from controller import adaugaSfarsit,parteRealaPrima,produsNumereSecventa,sumaNumereSecventa,adaugaPozitie,stergePoz,stergePozitii
from controller import inlocuireNumar,afiseazaPIPozitii
def testAfiseazaPozitii():
    l=[[1,0],[1,1],[3,4],[5,5]]
    assert afiseazaPIPozitii(l, 1, 2)==[1,4]
def testInlocuireNumar():
    l=[[1,1],[2,2],[1,1],[3,3],[1,1]]
    inlocuireNumar(l, [1,1], [0,0])
    assert l==[[0,0],[2,2],[0,0],[3,3],[0,0]]
def testProdusNumere():
    l=[[1,1],[1,1]]
    assert produsNumereSecventa(l, 0, 1)==[0,2]
def testModulNumar():
    assert modulNumar(1,1)==sqrt(2)
def testSumaNumere():
    l=[[1,0],[2,2]]
    assert sumaNumereSecventa(l, 0, 1)==[3,2]
def testSortare():
    l=[[0,1],[1,2],[0,3]]
    sortareLista(l)
    assert l==[[0,3],[1,2],[0,1]]
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
def testAdaugaPozitie():
    l=[[0,0],[1,0],[2,2],[3,3]]
    adaugaPozitie(l, 5, 5, 2)
    assert l==[[0,0],[1,0],[5,5],[2,2],[3,3]]
def testStergePoz():
    l=[[1,1],[3,3],[0,0]]
    stergePoz(l, 1)
    assert l==[[1,1],[0,0]]
def testStergePozitii():
    l=[0,1,2,3,4,5,6,7]
    stergePozitii(l, 1, 3)
    assert l==[0,4,5,6,7]
def teste():
    l=[[1,2],[3,4],[5,6],[6,8]]
    testAdaugaSfarsit()
    testModulNumar()
    parteRealaPrima(l)
    assert l==[[1,2],[6,8]]
    testPrim()
    testProdusNumere()
    testSumaNumere()
    testSortare()
    testAdaugaPozitie()
    testStergePoz()
    testStergePozitii()
    testInlocuireNumar()
    testAfiseazaPozitii()