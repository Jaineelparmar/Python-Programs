#MODULES AND PACKAGES PROGRAM
#Save file one.py in dummy folder and save two.py and dummy folder in one folder named as modules and packages


#SAVE THIS FILE AS one.py 
def test():
    print('Hello world')

def test1():
    print('Hello world1')

def test3():
    print('Hello world2')



#SAVE THIS FILE AS two.py
from dummy.one import test1,test3
test1()
test3()

#OR

from dummy import one
one.test()
one.test1()
one.test3()

