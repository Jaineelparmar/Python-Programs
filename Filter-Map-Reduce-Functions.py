#####################    MAP FUNCTION ##########################################

# filter(function, sequence) filters out in form of true and false
#To filter out even numbers from a list

def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

lst = [10,23,45,22,34,55,67,78]
lst1 = list(filter(is_even, lst))
print(lst1)

# same code using lamda function
lst = [10,23,45,22,34,55,67,78]
lst1 = list(filter(lambda x : (x%2==0), lst))
print(lst1)


#####################    MAP FUNCTION ##########################################

#map function = map(function, sequence)
#To find squares of elements from a list

def square(x):
        return x*x

lst = [1,2,3]
lst1 = list(map(square, lst))
print(lst1)

# same code using lamda function
lst = [1,2,3]
lst1 = list(map(lambda x : x*x, lst))
print(lst1)



#To find product of two lists

lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = list(map(lambda x, y : x*y, lst1, lst2))
print(lst3)


#####################    REDUCE FUNCTION ##########################################

#Reduce function = reduce(function, sequence) == it belongs to FUNCTOOLS module.
#Reduces a sequence of elements to a single value by processing the elements according to a function supplied.  
#To calculate products of elements from a list

from functools import *
lst = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x*y, lst)
print(result)
