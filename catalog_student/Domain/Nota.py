'''
Created on Nov 21, 2016

@author: Ursu
'''

class Nota:
    '''
    classdocs
    '''


    def __init__(self,idSt,idDis,valoare):
        '''
        Constructor
        '''
        self.__idSt = idSt
        self.__idDis = idDis
        self.__valoare = valoare

    def get_id_st(self):
        return self.__idSt


    def get_id_dis(self):
        return self.__idDis


    def get_valoare(self):
        return self.__valoare
    @staticmethod
    def readNota(line):
        line=line.split(",")
        gr=Nota(int(line[0]),int(line[1]),int(line[2]))
        return gr
    def __str__(self):
        return str(self.idSt)+' '+str(self.idDis)+' '+str(self.valoare)
    @staticmethod
    def writeNota(nota):
        return str(nota.idSt)+","+str(nota.idDis)+","+str(nota.valoare)
    idSt = property(get_id_st, None, None, None)
    idDis = property(get_id_dis, None, None, None)
    valoare = property(get_valoare, None, None, None)
    
    
    