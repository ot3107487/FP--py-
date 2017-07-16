'''
Created on Oct 29, 2016

@author: Ursu
'''
from UI import *
from tests import teste
from validator import conditieUndo
def run():
    l=[]
    categorii={"1":meniuAdauga,"2":meniuModifica,"3":meniuCauta,"4":meniuOperatii,"5":meniuFiltrare,"6":meniuUndo}
    while True:
        meniu()
        afisareLista(l)
        cmd=citireComanda()
        if conditieUndo(l1,l)==True:
            l1.append(list(l))
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
main()