'''
Created on Nov 14, 2016

@author: Ursu
'''
from Domain.Student import student
from Repository.Repository import RepositoryError
class StudentController:
    '''
    classdocs
    '''


    def __init__(self,repo,validator):
        '''
        Constructor
        '''
        self.__repo=repo
        self.__validator=validator
    def createStudent(self,ident,nume):
        '''
        Stocheaza un student in catalog:
        student(id,nume)
        '''
        st=student(ident,nume)
        self.__validator.valid(st)
        self.__repo.store(st)
        return st
    def removeStudent(self,ident):
        '''
        Sterge un student din Repository:
        student(id)
        '''
        st=self.__repo.findById(ident)
        self.__repo.remove(ident)
    def updateStudent(self,studentDTO):
        '''
        Modifica un student existent in Repository folosind un DTO (data transfer object)
        student(id) = studentDTO(id,nume)
        '''
        st=self.__repo.findById(studentDTO.ident)
        if studentDTO.nume!=None:
            st.nume=studentDTO.nume
        self.__repo.update(st)
    def __sortStudents(self, cond,students): 
        students.sort(key=cond)
        return students
    def getAllStudents(self):
        return self.__sortStudents(lambda x: x.ident,self.__repo.getAll())
    def findStudent(self,ident):
        l=self.getAllStudents()
        for x in l:
            if x.ident==ident:
                return x
        raise RepositoryError("Student not found")
        
        
            