'''
Created on Oct 29, 2016

@author: Ursu
'''
from utils import modulNumar,prim
from math import sqrt
from controller import adaugaSfarsit,parteRealaPrima

def testModulNumar():
    assert modulNumar(1,1)==sqrt(2)
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