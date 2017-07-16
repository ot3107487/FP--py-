'''
Created on Nov 14, 2016

@author: Ursu
'''

class student:
    '''
    classdocs
    '''


    def __init__(self, idStudent,numeSt):
        '''
        Constructor
        '''
        self.__ident=idStudent
        self.__nume=numeSt

    def get_ident(self):
        return self.__ident


    def get_nume(self):
        return self.__nume


    def set_ident(self, value):
        self.__ident = value


    def set_nume(self, value):
        self.__nume = value


    def del_ident(self):
        del self.__ident


    def del_nume(self):
        del self.__nume
    @staticmethod
    def readStudent(line):
        line= line.split(",")
        s= student(int(line[0]),line[1])
        return s
    @staticmethod
    def writeStudent(student):
        return str(student.ident)+","+student.nume

    ident = property(get_ident, set_ident, del_ident, None)
    nume = property(get_nume, set_nume, del_nume, None)
