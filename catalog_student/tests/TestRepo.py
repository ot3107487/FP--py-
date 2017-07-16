'''
Created on Dec 5, 2016

@author: Ursu
'''
import unittest
from Repository.Repository import Repository
from Domain.Student import student


class TestRepo(unittest.TestCase):


    def setUp(self):
        self.__repo=Repository()
        self.__entity=student(1,"Bogdan")

    def tearDown(self):
        del self.__repo
        del self.__entity


    def testRepo(self):
        assert len(self.__repo.getAll())==0
        self.__repo.store(self.__entity)
        assert self.__repo.findById(1).nume=="Bogdan"
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()