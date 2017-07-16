'''
Created on Nov 21, 2016

@author: Ursu
'''
from Domain.Nota import Nota
from Repository.Repository import RepositoryError

class NotaController:
    '''
    classdocs
    '''


    def __init__(self, strepo ,disrepo,notarepo,validator):
        '''
        Constructor
        '''
        self.__strepo = strepo
        self.__disrepo = disrepo
        self.__notarepo = notarepo
        self.__validator=validator
    def addNota(self,idSt,idDis,valoare):
        '''
        Stocheaza o nota in catalog:
        nota(id,,idSt,idDis,valoare)
        '''
        st=self.__strepo.findById(idSt)
        dis=self.__disrepo.findById(idDis)
        nota=Nota(idSt,idDis,valoare)
        self.__validator.valid(nota)
        self.__notarepo.storeNota(nota)
    def __sortNote(self,cond,nota): 
        nota.sort(key=cond)
        return nota
    def getStudentByID(self,idSt):
        return self.__strepo.findById(idSt).get_nume()
    def getDisciplinaByID(self,idDis):
        return self.__disrepo.findById(idDis).get_nume()
    def getStudentDisciplina(self,idDis):
        note=self.__notarepo.getAll()
        stnote=[]
        for x in self.__notarepo.getAll():
            if x.idDis==idDis:
                stud=self.__strepo.findById(x.idSt).get_nume()
                val=self.findNota(x.idSt, idDis)[2]
                stnote.append([stud,val])
        return stnote
    def __sortNoteRev(self,cond,nota):
        nota.sort(key=cond,reverse=True)
        return nota
    def getStudentDisciplinaNume(self,idDis):
        return self.__sortNote(lambda x:x[0],self.getStudentDisciplina(idDis))
    def getStudentDisciplinaNota(self,idDis):
        return self.__sortNoteRev(lambda x:x[1],self.getStudentDisciplina(idDis))
    def GetAllNote(self):
        '''
        returnneaza lista cu toate notele in ordinea id-ului
        '''
        return self.__sortNote(lambda x: x.idSt,self.__notarepo.getAll())
    def getStudentsAverage(self):
        note=self.GetAllNote()
        studentsnote={}
        best=[]
        for x in note:
            if x.idSt in studentsnote.keys():
                studentsnote[x.idSt][0]=studentsnote[x.idSt][0]+x.valoare
                studentsnote[x.idSt][1]=studentsnote[x.idSt][1]+1
            else:
                studentsnote[x.idSt]=[x.valoare,1]
        for x,y in studentsnote.items():
            medie=y[0]/y[1]
            best.append([x,medie])
        return best
    def getBestStudents(self):
        best=self.getStudentsAverage()
        return self.__sortNoteRev(lambda x:x[1],best)[:(len(best)//5+1)]
    def findNota(self,idSt,idDis):
        '''
        Gaseste nota studentului cu idSt la materia idDis
        Complexitatea este O(n)
        '''
        l=self.GetAllNote()
        for x in l:
            if int(x.get_id_st())==idSt and int(x.get_id_dis())==idDis:
                student=self.__strepo.findById(x.get_id_st())
                disciplina=self.__disrepo.findById(x.get_id_dis())
                return student.get_nume(),disciplina.get_nume(),x.get_valoare()
        raise RepositoryError("Grade doesn't exist")