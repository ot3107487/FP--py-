'''
Created on Nov 14, 2016

@author: Ursu
'''
from Validators.StudentValidator import StudentValidator
from Repository.Repository import Repository
from Controller.StudentController import StudentController
from UI.StudentUI import StudentUI
from Validators.DisciplinaValidator import DisciplinaValidator
from UI.DisciplinaUI import DisciplinaUI
from Controller.DisciplinaController import disciplinaController
from Validators.NotaValidator import NotaValidator
from Controller.NotaController import NotaController
from UI.NotaUI import NotaUI
from UI.StatisticiUI import StatisticiUI
from Repository.FileRepository import FileRepository
from Domain.Student import student
from Domain.Disciplina import disciplina
from Domain.Nota import Nota
from Utils.Sortari import teste
srepo=FileRepository("C:\\Users\\bogda\\Desktop\\pyth\\catalog_student\\Students.txt",student.readStudent,student.writeStudent)
val=StudentValidator()
ctr=StudentController(srepo,val)
studUI=StudentUI(ctr)
disrepo=FileRepository("C:\\Users\\bogda\\Desktop\\pyth\\catalog_student\\Subjects.txt",disciplina.readDisciplina,disciplina.writeDisciplina)
disval=DisciplinaValidator()
disctr=disciplinaController(disrepo,disval)
disUI=DisciplinaUI(disctr)
notarepo=FileRepository("C:\\Users\\bogda\\Desktop\\pyth\\catalog_student\\Note.txt",Nota.readNota,Nota.writeNota)
nval=NotaValidator()
nctr=NotaController(srepo,disrepo,notarepo,nval)
notaUI=NotaUI(nctr)
statistici=StatisticiUI(nctr)

def meniu():
    print("Students-to acces students")
    print("Subjects-to acces subjects")
    print("Grades-to acces grades")
    print("Statistics-to acces statistics")
    print("Exit-to close the application")
def run():
    while True:
        meniu()
        cmd=input("Type command:")
        if cmd=="Students":
            studUI.showStudentUI()
        if cmd=="Subjects":
            disUI.showDisciplinaUI()
        if cmd=="Grades":
            notaUI.showNotaUI()
        if cmd=="Statistics":
            statistici.showStatisticiUI()
        if cmd=="Exit":
            print("Bye bye")
            return
teste()
run()
        