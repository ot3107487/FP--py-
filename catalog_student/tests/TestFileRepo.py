'''
Created on Dec 5, 2016

@author: Ursu
'''
import unittest
from Repository.FileRepository import FileRepository
from Domain.Student import student


class TestFileRepo(unittest.TestCase):


    def setUp(self):
        self.__repo=FileRepository("C:\\Users\\bogda\\Desktop\\pyth\\catalog_student\\Students.txt",student.readStudent,student.writeStudent)
        self.__entity=student(101,"Bogdan")
        

    def tearDown(self):
        del self.__repo
        del self.__entity

    def testFileRepo(self):
        self.__repo.remove(101)
        self.__repo.store(self.__entity)
        assert (self.__repo.findById(101).nume=="Bogdan")
        l=len(self.__repo.getAll())
        self.__repo.remove(101)
        assert len(self.__repo.getAll())==l-1

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()