#Sum of all elements from a list of integers using FOR LOOP .

li = [10,20,30,40]
sum = 0
for i in li:
    sum += i
print('sum = ',sum)
print('-'*20)

#OR

lst = [10,20,30,40,50]
sum = 0
for i in range(len(lst)):
    sum += lst[i]
print('sum = ',sum)
print('-'*20)


#Sum of all individual digits from a list of integers.

li = [120, 44, 68, 17750, 17, 3, 80]
total = 0
for num in li:
    for digit in str(num):
        total += int(digit)
print('Sum of all individual digits from a list of integers is: '+str(total))



#Sum of even elements from a list.

def sum_of_odd(li):
    sum = 0
    for i in li:
        if (i % 2 == 0) :
            sum += i
    return sum
    
x = [1, 3, 4, 5, 6, 7, 8]
print(sum_of_odd(x))



#Sum of odd elements from a list.

def sum_of_odd(li):
    sum = 0
    for i in li:
        if (i % 2 != 0) :
            sum += i
    return sum
    
x = [1, 3, 4, 5, 6, 7]
print(sum_of_odd(x))



#Sum of all even numbers between 1 to n.
n = int(input('Enter a number:'))
t = 0 
for i in range(1,n+1):
    if (i%2 == 0):
        t = t+i
print(t)



#Sum of all odd numbers between 1 to n.
n = int(input('Enter a number:'))
t = 0 
for i in range(1,n+1):
    if (i%2 != 0):
        t = t+i
print(t)


