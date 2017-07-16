'''
Created on Nov 14, 2016

@author: Ursu
'''
#from Domain.Student import student
class StudentValidException(Exception):
    pass
class StudentValidator:
    '''
    Verifica daca un student a fost introdus corect:
    id - diefrit de ""
    nume - diferit de ""
    '''
    @staticmethod
    def valid(student):
        erori=[]
        if(student.ident==""):
            erori.append("Id-ul nu poate fi gol")
        if(student.nume==""):
            erori.append("Numele nu poate fi vid ")
        if(len(erori)>0):
            raise StudentValidException(erori)
        
        