#Maximum number from a list.

def max_of_list(li):
    final = li[0]
    for i in li:
        if i > final:
            final = i
    return final

x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(max_of_list(x))




#Maximum of three numbers.

def max_of_three(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    else:
        return c
print(max_of_three(10, 20, 30))

#or

def max_of_three(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    else:
        return c
res = max_of_three(10, 20, 30)
print(res)



#Maximum of three negative numbers.

def max_of_three(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    else:
        return c
res = max_of_three(-10, -20, -30)
print(res)

#or

def max_of_three(a, b, c):
    if a>b and a>c:
        return a
    elif b>a and b>c :
        return b
    else:
        return c
print(max_of_three(-10, -20, -30))
