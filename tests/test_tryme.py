from icecream import ic
from unittest import TestCase
from pytest import mark
from pytest_dependency import depends

class MyTests(TestCase):
    @mark.order(4)
    @mark.dependency()
    def test1(self):
        ic(f'Running {self._testMethodName}')
        #assert False
    
    @mark.order(3)
    @mark.dependency(depends=['MyTests::test1'])
    def test2(self):
        ic(f'Running {self._testMethodName}')
    
    @mark.order(2)
    #@mark.dependency()
    def test3(self):
        ic(f'Running {self._testMethodName}')
    
    @mark.order(1)
    #@mark.dependency()
    def test4(self):
        ic(f'Running {self._testMethodName}')