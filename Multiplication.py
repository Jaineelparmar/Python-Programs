# Multiplication table from 1 to 25.

for x in range(1,26):
    for y in range(1,11):
        print(x,'x',y,'=',str(x*y))
    print('-'*20)



# Multiplication table for any number using input function.

n = int(input('enter a number:'))
for i in range(1, 11):
    print(n,'x',i,'=',str(n*i))
