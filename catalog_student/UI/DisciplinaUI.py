'''
Created on Nov 14, 2016

@author: Ursu
'''
from Repository.Repository import RepositoryError
from Validators.DisciplinaValidator import DisciplinaValidatorException
from Domain.DisciplinaDTO import disciplinaDTO

class DisciplinaUI:
    def __init__(self, ctr):
        '''
        Constructor
        '''
        self.__ctr=ctr 
    def __showAllDiscipline(self):
        discipline=self.__ctr.GetAllDiscipline()
        if len(discipline)==0:
            print("No subjects in catalog")
        else:
            print("Id Name  Profesor")
        for x in discipline:
            print(x.get_ident(),x.get_nume(),x.get_profesor())
    def __addDisciplina(self):
        ident=int(input("Insert subject's id: "))
        nume=input("Insert subject's name: ")
        profesor=input("Insert subject's teacher: ")
        try:
            di=self.__ctr.createDisciplina(ident,nume,profesor)
            print("Subject "+di.get_nume()+" stored...")
        except RepositoryError as exp:
            print(exp)
        except DisciplinaValidatorException as exp:
            print(exp)
    def __removeDisciplina(self):
        ident=int(input("Insert subject's id: "))
        try:
            self.__ctr.removeDisciplina(ident)
        except RepositoryError as exp:
            print(exp)
    def __updateDisciplina(self):
        ident=int(input("Insert the subject's id you want to update: "))
        newname=input("Insert the new name you want to update with: ")
        newprof=input("Insert the new teacher you want to update with: ")
        diDTO=disciplinaDTO(ident,newname,newprof)
        try:
            self.__ctr.updateDisciplina(diDTO)
        except RepositoryError as exp:
            print(exp)
    def __findDisciplina(self):
        nume=input("Insert the subject's name you want to find:")
        try:
            di=self.__ctr.findDisciplina(nume)
            print("ID:"+str(di.get_ident())+'\n'+"Nume:"+di.get_nume()+"\nProfesor:"+di.get_profesor())
        except RepositoryError as exp:
            print(exp)
    @staticmethod
    def meniu():
        print("Chosse a command:")
        print("Add , View , Remove , Update , Find , Exit")
    def showDisciplinaUI(self):
        while True:
            DisciplinaUI.meniu()
            cmd=input()
            if cmd=="Add":
                self.__addDisciplina()
            if cmd=="View":
                self.__showAllDiscipline()
            if cmd=="Remove":
                self.__removeDisciplina()
            if cmd=="Update":
                self.__updateDisciplina()
            if cmd=="Find":
                self.__findDisciplina()
            if cmd=="Exit":
                return