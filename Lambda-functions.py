#Anonymous funtion = lambdas
#A function without a name is called an anonymous function.


# lamda argument_list : expression   (eg. lambda x : x*x)
#returns a square value of a given number.

f = lambda x: x*x
value = f(5)
print('square of 5=',value)



#lamda function to calculate sum of two numbers
f = lambda x, y: x+y
result = f(1.4, 3.4)
print('sum =',result)



#lamda function to calculate sum of two numbers

max = lambda x, y : x if x>y else y
a, b = [int(n) for n in input('enter two numbers:').split(',')]
print('bigger number=',max(a,b))

