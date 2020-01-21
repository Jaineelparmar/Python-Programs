#Using For loop for printing only odd numbers

#Using equal to operator
li=[1,2,3,4,5,6,7,8,9,10]
x = []
for num in li:
    if (num % 2 == 1) :
        x.append(num)
print(x)

#OR

#Using not equal to operator
li=[1,2,3,4,5,6,7,8,9,10]
x = []
for num in li:
    if (num % 2 != 0) :
        x.append(num)
print('List of odd numbers =', x)



