'''
Created on Nov 14, 2016

@author: Ursu
'''
class DisciplinaValidatorException(Exception):
    pass
class DisciplinaValidator:
    '''
    Valideaza daca o disciplina este introdusa corect:
    id - nu trebuie sa fie gol
    numele- nutrebuie sa fie gol
    profesorul - nu trebuie sa fie gol
    '''
    @staticmethod
    def valid(disciplina):
        erori=[]
        if(disciplina.ident==""):
            erori.append("Id-ul nu poate fi gol")
        if(disciplina.nume==""):
            erori.append("Numele nu poate fi vid")
        if(disciplina.profesor==""):
            erori.append("Profesorul trebuie sa aiba un nume")
        if(len(erori)>0):
            raise DisciplinaValidatorException(erori)