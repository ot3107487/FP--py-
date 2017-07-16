'''
Created on Nov 14, 2016

@author: Ursu
'''
from Domain.Student import student

class RepositoryError(Exception):
    pass
class Repository:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._entities={}
    def store(self,entity):
        '''
        Salveaza un obiect (entitate) in Repository cu conditia ca acesta sa nu existe deja
        '''
        if entity.ident in self._entities: 
            raise RepositoryError("ID is already in repository")
        self._entities[entity.ident]=entity
    def storeNota(self,entity):
        idDis=entity.idDis
        idSt=entity.idSt
        nota=(idSt,idDis)
        if nota in self._entities:
            raise RepositoryError("Grade already assigned")
        self._entities[entity.idSt,entity.idDis]=entity
    def remove(self,ident):
        '''
        Sterge un obiect (entitate) din Repository cu conditia ca acesta sa existe 
        '''
        if ident not in self._entities:
            raise RepositoryError("Id not found")
        del self._entities[ident]
    def update(self,entity):
        '''
        Modifca un obiect (entitate) din Repository cu conditia ca acesta sa existe 
        cu un alt obiect
        '''
        if entity.ident not in self._entities:
            raise RepositoryError("Can't update what doesn't exist!")
        self._entities[entity.ident]=entity
    def getAll(self):
        '''
        Returneaza o lista cu toate entitatile din Repository
        '''
        l=[]
        for i in self._entities.values():
            l.append(i)
        return l
   
    def findById(self,ident):
        '''
        Gaseste o entitate in Repository dupa ID
        '''
        if ident not in self._entities:
            raise RepositoryError("Id not found")
        return self._entities[ident]
    def __add__(self,entity):
        self.store(entity)
    def __radd__(self,entity):
        self.store(entity)
    def __sub__(self,entity):
        if type(entity) is int:
            self.remove(entity)
        else:
            self.remove(entity.ident) 
    
    def __rsub__(self,entity):
        self.__sub__(entity)
    def __len__(self):
        return len(self._entities)
        
def testRepository():
    repo = Repository()
    assert(len(repo)==0)
    st1=student("1","Ioan Bogdan")
    repo.store(st1)
    assert(len(repo)==1)
    st2=student("2","Alexandru Ivanov")
    repo+st2
    assert(len(repo)==2)
    st3=student("2","Fulea Razvan")
    try:
        repo.store(st3)
        assert False
    except RepositoryError:
        pass
    repo-st1
    st2-repo
    assert(len(repo)==0)
    
testRepository()

        
        