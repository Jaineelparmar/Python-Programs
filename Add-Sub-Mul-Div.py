#results of addition,subtraction,division,multiplication.

def sum_sub_div_mul(a, b):
    c = a+b
    d = a-b 
    e = a*b 
    f = a/b 
    return c, d, e, f

x = 10
y = 5
print(sum_sub_div_mul(x, y))

#or

def sum_sub_div_mul(a, b):
    c = a+b
    d = a-b 
    e = a*b 
    f = a/b 
    return c, d, e, f

x = sum_sub_div_mul(10, 5)
print(x)

#or

def sum_sub_div_mul(a, b):
    c = a+b
    d = a-b 
    e = a*b 
    f = a/b 
    return c, d, e, f

x = sum_sub_div_mul(10, 5)
print('The results are:')
for i in x:
    print(i)
