'''
Created on Nov 14, 2016

@author: Ursu
'''

class disciplinaDTO:
    '''
    classdocs
    '''


    def __init__(self, idDisciplina,numeDi,profesor):
        '''
        Constructor
        '''
        self.__ident=idDisciplina
        self.__nume=numeDi
        self.__profesor=profesor

    def get_ident(self):
        return self.__ident


    def get_nume(self):
        return self.__nume


    def get_profesor(self):
        return self.__profesor


    def set_ident(self, value):
        self.__ident = value


    def set_nume(self, value):
        self.__nume = value


    def set_profesor(self, value):
        self.__profesor = value


    def del_ident(self):
        del self.__ident


    def del_nume(self):
        del self.__nume


    def del_profesor(self):
        del self.__profesor
    @staticmethod
    def readDisciplina(line):
        line= line.split(",")
        d= disciplinaDTO(int(line[0]),line[1],line[2])
        return d
    @staticmethod
    def writeDisciplina(disciplina):
        return str(disciplina.ident)+","+disciplina.nume+disciplina.profesor

    ident = property(get_ident, set_ident, del_ident, None)
    nume = property(get_nume, set_nume, del_nume, None)
    profesor = property(get_profesor, set_profesor, del_profesor, None)

   
        