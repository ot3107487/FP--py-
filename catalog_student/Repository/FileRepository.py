'''
Created on Dec 4, 2016

@author: Ursu
'''
from Repository.Repository import Repository

class FileRepository(Repository):
    '''
    classdocs
    '''


    def __init__(self, filename,readEntity,writeEntity):
        '''
        Constructor
        '''
        Repository.__init__(self)
        self.__filename = filename
        self.__readEntity= readEntity
        self.__writeEntity= writeEntity
        self.__readFromFile()
        
    def __readFromFile(self):
        with open(self.__filename) as f:
            content = f.readlines()
            for line in content:
                if line!="\n":
                    entity = self.__readEntity(line)
                    try:
                        self._entities[entity.ident]=entity
                    except AttributeError:
                        self._entities[entity.idSt,entity.idDis]=entity
    def __writeToFile(self):
        f = open(self.__filename,'w')
        for entity in self._entities.values():
            f.write(self.__writeEntity(entity)+"\n") 
        f.close() 
    
    def store(self,entity):
        Repository.store(self, entity)
        self.__writeToFile()
    def storeNota(self, entity):
        Repository.storeNota(self, entity)
        self.__writeToFile()
        
    def remove(self,ident):
        Repository.remove(self, ident)
        self.__writeToFile()
       
        
    def update(self,entity):
        Repository.update(self, entity)
        self.__writeToFile()
    
    def close(self):
        self.__writeToFile()