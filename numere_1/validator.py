'''
Created on Oct 29, 2016

@author: Ursu
'''
def validPoz(l,poz):
    if poz>len(l) or poz<0:
        raise ValueError("Pozitie incorecta")
def validPozitii(l,st,dr):
    if st>dr or dr>len(l) or dr<0 or st<0:
        raise ValueError("Pozitii incorecte")
def conditieUndo(l1,l):
    '''
    Verifica daca lista l  este deja in lista l1
    '''
    if len(l1)>0 and l1[len(l1)-1]==l:
        return False
    return True