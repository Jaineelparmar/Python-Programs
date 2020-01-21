####  FUNCTION DECORATORS  ####

# A (DECORATOR) is a function that accepts function as a parameter and returns a function.
# A (DECORATOR) takes the result of a function, modifies the result and returns it.
# Thus decorators are useful to perform some additional processing required by a function.

'''syntax of decorators which are equivalent to each other
@dec1
@dec2
def func(arg1, arg2,...):
    pass

#or

def func(arg1, arg2,...):
    pass
func = dec1(dec2(func))
'''


#A decorator to increase value by 2

def decor(fun):                         #this is the decorator function
    def inner():                        #inner function that modifies
        value = fun()                   #access value returned by fun()
        return value+2                  #increase the value by 2
    return inner                        #return the inner function

def num():                              #a function to which decorator is applied
    return 10


#Call decorator function and pass num
result_fun = decor(num)                 # it represents inner function
print(result_fun())                     #call result_fun and display the result




#Apply decorator to a function using @symbol

def decor(fun):                         #this is the decorator function
    def inner():                        #inner function that modifies
        value = fun()                   #access value returned by fun()
        return value+2                  #increase the value by 2
    return inner                        #return the inner function

@decor
def num():                              #a function to which decorator is applied
    return 10

print(num())                            #call num() function and display its result





#To create two decorators

def decor(fun):                         #this is the decorator function
    def inner():                        #inner function that modifies
        value = fun()                   #access value returned by fun()
        return value+2                  #increase the value by 2
    return inner                        #return the inner function


def decor1(fun):                         #this is the decorator function
    def inner():                        #inner function that modifies
        value = fun()                   #access value returned by fun()
        return value*2                  #multiply the value by 2
    return inner                        #return the inner function


def num():
    return 10

result_fun = decor(decor1(num))
print(result_fun())




#To apply two decorators to same function using @symbol.
def decor(fun):                         #this is the decorator function
    def inner():                        #inner function that modifies
        value = fun()                   #access value returned by fun()
        return value+2                  #increase the value by 2
    return inner                        #return the inner function


def decor1(fun):                         #this is the decorator function
    def inner():                        #inner function that modifies
        value = fun()                   #access value returned by fun()
        return value*2                  #multiply the value by 2
    return inner                        #return the inner function

@decor
@decor1
def num():
    return 10

print(num())


