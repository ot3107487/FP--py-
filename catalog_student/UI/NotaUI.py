'''
Created on Nov 21, 2016

@author: Ursu
'''
from Repository.Repository import RepositoryError
from Validators.NotaValidator import NotaError, NotaValidator

class NotaUI:
    def __init__(self, ctr):
        '''
        Constructor
        '''
        self.__ctr=ctr 
    def __showAllNote(self):
        note=self.__ctr.GetAllNote()
        if len(note)==0:
            print("No grades in catalog")
        else:
            print("Student       Object      Grade       ")
        for x in note:
            print(self.__ctr.getStudentByID(x.get_id_st()),self.__ctr.getDisciplinaByID(x.get_id_dis()),x.get_valoare())
    def __addNota(self):
        idSt=int(input("Insert student's id: "))
        idDis=int(input("Insert subject's id: "))
        valoare=int(input("Insert grade's value: "))
        try:
            nota=self.__ctr.addNota(idSt,idDis,valoare)
            print("Grade assigned...")
        except RepositoryError as exp:
            print(exp)
        except NotaError as exp:
            print(exp)
    def __findNota(self):
        idSt=int(input("Insert student's id:"))
        idDis=int(input("Insert object's id"))
        try:
            nota=self.__ctr.findNota(idSt,idDis)
            print("Student:"+nota[0]+"\nObject:"+nota[1]+"\nGrade:"+str(nota[2]))
        except RepositoryError as exp:
            print(exp)
    @staticmethod
    def meniu():
        print("Chosse a command:")
        print("Add , View , Find , Exit")
    def showNotaUI(self):
        while True:
            NotaUI.meniu()
            cmd=input()
            if cmd=="Add":
                self.__addNota()
            if cmd=="View":
                self.__showAllNote()
            if cmd=="Find":
                self.__findNota()
            if cmd=="Exit":
                return