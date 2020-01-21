#Even and Odd numbers.

a=10
if (a%2==0):
    print(str(a)+',is an even number')
else :
    print(str(a)+',is an odd number')

########################################

a=101
if (a%2==0):
    print(str(a)+',is an even number')
else :
    print(str(a)+',is an odd number')


########################################
#Using Input function.

a= int(input('enter a number:'))
if (a%2==0):
    print(str(a)+',is an even number')
else :
    print(str(a)+',is an odd number')


#even or odd numbers using functions
def even_or_odd(num):
    if num%2 == 0:
        return 'even'
    else:
        return 'odd'
x = int(input('enter a number:'))
print(even_or_odd(x))

