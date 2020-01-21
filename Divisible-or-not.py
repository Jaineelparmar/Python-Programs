#To check if the number is divisible by 3 and 5 or anyone of them.

a = 30
if (a%3==0) and (a%5==0):
    print(str(a)+' is divisible by both Three and Five')
elif (a%5==0) :
    print(str(a)+' is divisible by Five')
elif (a%3==0) :
    print(str(a)+' is divisible by Three')
else:
    print(str(a)+' is not divisible by Three and Five')

    
#Using Input function.
a = int(input('Enter a number:'))
if (a%3==0) and (a%5==0):
    print(str(a)+' is divisible by both Three and Five')
elif (a%5==0) :
    print(str(a)+' is divisible by Five')
elif (a%3==0) :
    print(str(a)+' is divisible by Three')
else:
    print(str(a)+' is not divisible by Three and Five')



#Print all integers which are divisible by 5 or 7 from a list of integers.

# FOR 5 AND 7
li = [10,15,35,40,42,39,58,70,105,678]
for i in li:
    if i%5==0 and i%7==0:
        print(i)


# FOR 5 OR 7
li = [10,15,35,40,42,39,58,70,105,678]
for i in li:
    if i%5==0 or i%7==0:
        print(i)


#OR
a = int(input('enter a number:'))
if a%7 == 0  and a%5==0:
    print(a,'is divisible by 5 and 7')
elif a%5==0:
    print(a,'is divisible by 5')
elif a%7==0:
    print(a,'is divisible by 7')
else:
    print(a,'is not divisible by 5 and 7')

