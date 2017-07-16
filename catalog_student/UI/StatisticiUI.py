'''
Created on Nov 26, 2016

@author: Ursu
'''
from Repository.Repository import RepositoryError

class StatisticiUI:
    '''
    classdocs
    '''
    def __init__(self,ctr):
        self.__ctr=ctr
    @staticmethod
    def meniu():
        print("1.View list of students sorted by name")
        print("2.View list of students sorted by grade")
        print("3.View first 20% best students")
    def showStatisticiUI(self):
        while True:
            StatisticiUI.meniu()
            print("1,2,3,Exit")
            print("Type command:")
            cmd=input()
            if cmd=="1":
                idDis=int(input("Insert subject's id:"))
                try:
                    lista=self.__ctr.getStudentDisciplinaNume(idDis)
                except RepositoryError as exp:
                    print(exp)
                for x in lista:
                    print(x[0]+' '+str(x[1])+'\n')
            if cmd=="2":
                idDis=int(input("Insert subject's id:"))
                try:
                    lista=self.__ctr.getStudentDisciplinaNota(idDis)
                except RepositoryError as exp:
                    print(exp)
                for x in lista:
                    print(x[0]+' '+str(x[1])+'\n')
            if cmd=="3":
                try:
                    best=self.__ctr.getBestStudents()
                except ZeroDivisionError as exp:
                    print(exp)
                for x in best:
                    print(str(x[0])+' '+str(x[1])+'\n')
            if cmd=="Exit":
                return
        
        