####### FORMAL AND ACTUAL ARGUMENTS.
def sum(a, b):
    c = a+b
    return c
x =10; y =15
print(sum(x, y))


#POSITIONAL ARGUMENT
#positional argument function

def attach(s1, s2):
    s3 = s1+s2
    print('complete string: '+s3)

attach('new', 'york')

#or

def attach(s1, s2):
    s3 = s1+s2
    return s3  

print('complete string:'+attach('new', 'york'))



#KEYWORD ARGUMENT
#keyword argument function

def grocery(item, price):
    return 'item ='+ item + '\n' + 'price ='+ str(price)

print(grocery('kmgr', 450.0))

#OR

def grocery(item, price):
    print('Item = %s' %item)
    print('Price = %.2f' %price)

grocery(item = 'sugar' , price = 50.75)
grocery(price = 88.00, item='oil')



#DEFAULT ARGUMENT
#Default argument function

def grocery(item, price=40.00):
    print('Item = %s' %item)
    print('Price =%.2f' %price)

grocery(item = 'sugar', price = 50.46)
grocery(item = 'sugar')



#VARIABLE LENGTH ARGUMENT
#variable length argument function

def add(farg, *args):
    print('formal argument= ',farg)

    sum = 0
    for i in args:
        sum += i
    print('sum of all numbers= ',(farg+sum))

add(5, 10) 
add(5, 10, 20, 30)
