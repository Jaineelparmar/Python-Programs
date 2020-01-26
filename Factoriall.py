#factorial
def factorial_or_not(n):
    prod = 1
    while n >= 1:
        prod *= n
        n -= 1

    return prod

for i in range(1,11):
    print('factorial of {} is {}'.format(i, factorial_or_not(i)))



### Recursive function - that calls itself

#to calculate factorial using recursive function

def factorial_or_not(n):

    if n == 0:
        result= 1
    else:
        result=n*factorial_or_not(n-1)

    return result

for i in range(1,11):
    print('factorial of {} is {}'.format(i,factorial_or_not(i)))

