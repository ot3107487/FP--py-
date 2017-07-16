'''
Created on Nov 14, 2016

@author: Ursu
'''
from Repository.Repository import RepositoryError
from Validators.StudentValidator import StudentValidException
from Domain.StudentDTO import studentDTO

class StudentUI:
    def __init__(self, ctr):
        '''
        Constructor
        '''
        self.__ctr=ctr 
    def __showAllStudents(self):
        students=self.__ctr.getAllStudents()
        if len(students)==0:
            print("No students in catalog")
        else:
            print("Id|Name")
        for x in students:
            print(x.get_ident(),'|',x.get_nume())
    def __addStudent(self):
        ident=int(input("Insert student's id: "))
        nume=input("Insert student's name: ")
        try:
            st=self.__ctr.createStudent(ident,nume)
            print("Student "+st.get_nume()+" stored...")
        except RepositoryError as exp:
            print(exp)
        except StudentValidException as exp:
            print(exp)
    def __removeStudent(self):
        ident=int(input("Insert student's id: "))
        try:
            self.__ctr.removeStudent(ident)
        except RepositoryError as exp:
            print(exp)
    def __updateStudent(self):
        ident=int(input("Insert the student's id you want to update: "))
        newname=input("Insert the new name you want to update with: ")
        stDTO=studentDTO(ident,newname)
        try:
            self.__ctr.updateStudent(stDTO)
        except RepositoryError as exp:
            print(exp)
    def __findStudent(self):
        ident=int(input("Insert student's id you want to see:"))
        try:
            st=self.__ctr.findStudent(ident)
            print("ID:"+str(st.get_ident())+'\n'+"Name:"+st.get_nume())
        except RepositoryError as exp:
            print(exp)
    @staticmethod
    def meniu():
        print("Chosse a command:")
        print("Add , View , Remove , Update , Find, Exit")
    def showStudentUI(self):
        while True:
            StudentUI.meniu()
            cmd=input()
            if cmd=="Add":
                self.__addStudent()
            if cmd=="View":
                self.__showAllStudents()
            if cmd=="Remove":
                self.__removeStudent()
            if cmd=="Update":
                self.__updateStudent()
            if cmd=="Find":
                self.__findStudent()
            if cmd=="Exit":
                return