'''
Created on Nov 14, 2016

@author: Ursu
'''
from Domain.Disciplina import disciplina
from Repository.Repository import RepositoryError
class disciplinaController:
    '''
    classdocs
    '''


    def __init__(self,repo,validator):
        '''
        Constructor
        '''
        self.__repo=repo
        self.__validator=validator
    def createDisciplina(self,ident,nume,profesor):
        '''
        Stocheaza in Repository o discplina care nu este deja prezenta:
        disciplina(id,nume , profesor)
        '''
        di=disciplina(ident,nume,profesor)
        self.__validator.valid(di)
        self.__repo.store(di)
        return di
    def removeDisciplina(self,ident):
        '''
        Sterge din Repository o disciplina daca ceasta exista:
        disciplina(id)
        '''
        di=self.__repo.findById(ident)
        self.__repo.remove(ident)
    def updateDisciplina(self,disciplinaDTO):
        '''
        Modifica o disciplina existenta in Repository folosind un DTO (data transfer object)
        disciplina(id) = disciplinaDTO(id,nume,profesor)
        '''
        di=self.__repo.findById(disciplinaDTO.ident)
        if disciplinaDTO.nume!=None:
            di.nume=disciplinaDTO.nume
        if disciplinaDTO.profesor!=None:
            di.profesor=disciplinaDTO.profesor
        self.__repo.update(di)
    def __sortDisciplina(self,cond,disciplina): 
        disciplina.sort(key=cond)
        return disciplina
    def findDisciplina(self,nume):
        '''
        Returneaza disciplina cu numele nume dat ca parametru
        '''
        l=self.GetAllDiscipline()
        for x in l:
            if x.get_nume()==nume:
                return x
        raise RepositoryError("Object not found")
    def GetAllDiscipline(self):
        '''
        returnneaza lista cu toate materiile in ordinea id-ului
        '''
        return self.__sortDisciplina(lambda x:x.ident,self.__repo.getAll())