'''
Created on Oct 29, 2016

@author: Ursu
'''
from UI import *
from tests import *

def run():
    l=[]
    l1=[]
    categorii={"1":meniuAdauga,"2":meniuModifica,"3":meniuCauta,"4":meniuOperatii,"5":meniuFiltrare}
    while True:
        meniu()
        afisareLista(l)
        cmd=citireComanda()
        if cmd=="6":
            try:
                print(l1)
            except ValueError:
                print("Imposibil de realizat Undo")
        if cmd=="x":
            return
        if cmd in categorii:
            try:
                categorii[cmd](l)
                l1.append(l)
            except ValueError as ex:
                print(ex)            
        else:
            print("Command error! Insert sth else")
    
def main():
    teste()
    run()
main()