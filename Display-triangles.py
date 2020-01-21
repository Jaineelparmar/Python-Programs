#To display equilateral triangle
n = 40                           
for i in range(1,11):
    print(' '*n, end='')
    print('* '*(i))
    n-=1
    
#OR

n = 40
for i in range(1,11):
    print(' '*(n-i) + '* '*(i))

#OR

def pyfunc(n):
    for i in range(n):
        print(' '*(n-i)+'* '*(i))    
pyfunc(int(input('enter upto?')))



#To display right angled triangle

for i in range(1,11):
    for j in range(1,i+1):
        print('*',end='')
    print()


for i in range(1,11):
    print('*' *(i))

