# GLOBAL AND LOCAL VARIABLES

a = 1
def myfunction():
    a = 2
    print('local variable a =',a)
myfunction()
print('global variable a =',a)



#global variable inside a function

a = 1
def myfunction():
    global a
    print('old global a =',a)
    a = 2
    print('new global a =',a)
print(a)
myfunction()
print(a)



#to get a copy of global variable inside a function and work with it.

a = 1                                   #global var
def myfunction():
    a = 2                               #local var
    x = globals()['a']                  # get global var into x
    print('global var a = ',x)
    print('local var a= ',a)
myfunction()
print('global var a= ',a)

