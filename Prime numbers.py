#Prime or not

def prime_or_not(n):
    x  = 1
    for i in range(2, n):
        if n%i == 0:
            x = 0
            break
        else:
            x = 1
    return x

num = int(input('enter a number:'))
result = prime_or_not(num)
if result == 1:
    print(num,'is prime')
else:
    print(num,'is not prime')



#to generate how many prime numbers.

def prime(n):
    x = 1
    for i in range(2, n):
        if n% i == 0:
            x = 0
            break
        else:
            x = 1
    return x

num = int(input('enter a number:'))
i = 2
c = 1
while True:
    if prime(i):
        print(i)
        c += 1
    i += 1
    if c > num:
        break

