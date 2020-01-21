#Sum of integers in a list

lst = [10,20,30,40,50]
sum = 0
i = 0
while i< len(lst):
    sum += lst[i]
    i += 1
print('sum = ',sum)
print('-'*20)
	

#Sum of first and last digit of any number using while loop

a = int(input('Enter a number:'))
b = a%10
c = a
while c >= 10:
    c = c/10
print(int(b)+int(c))



#Sum of all individual digits from a number

num = int(input('enter any number:'))
sum = 0
while(num > 0):
    r = num % 10
    sum += r
    num //= 10
print('Sum of all individual digits from a number is: '+str(sum))



