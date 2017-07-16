'''
Created on Nov 21, 2016

@author: Ursu
'''
class NotaError(Exception):
    pass
class NotaValidator:
    '''
    classdocs
    '''

    @staticmethod
    def valid(nota):
        s=""
        if float(nota.get_valoare())<0 or float(nota.get_valoare())>10:
            s+="Invalid Note!"
            raise NotaError(s)
        
        