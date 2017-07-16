'''
Created on Oct 29, 2016

@author: Ursu
'''
from math import sqrt

def citesteIntSecure(mesaj):
    while True:
        try:
            n=int(input(mesaj))
            return n
        except ValueError:
            print("Introduceti o valoare numerica intreaga")
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
def citireComanda():
    return input("Introduceti comanda: ")

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