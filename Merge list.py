#Merge two lists of equal lengths.

def merge_lists(one, two):
    final = []
    for i in range(len(one)):
        final.append(one[i])
        final.append(two[i])
    return final
x = [1, 2, 3] 
y = ['a', 'b', 'c'] 
print(merge_lists(x, y)) 



#Merge two list
def add (a,b):
    z = []
    for i in range(len(a)):
            z.append(a[i])
            z.append(b[i])
    return z

x = [1,3,5,7,9]
y = [2,4,6,8,10]
print(add(x, y))

#OR

#Merge two list
def add (a,b):
    z = []
    a = set(x)
    b = set(y)
    z = a.union(b)
    return z

x = [1,3,5,7,9]
y = [2,4,6,8,10]
print(list(add(x, y)))



#Merge two lists of different lengths.

def merge_lists(one, two):
    final = []

    shorter = one if len(two) > len(one) else two
    longer = one if len(one) > len(two) else two
 
    for i in range(len(shorter)):
        final.append(one[i])
        final.append(two[i])
        
    return final +longer[i+1:]

x = [1, 2, 3, 4] 
y = ['a', 'b', 'c','d','e','f'] 
print(merge_lists(x, y))

# OR

def merge_lists(one, two):
    final = []
    
    if len(one) > len(two):
        longer =one
        shorter=two
    else:
        longer = two
        shorter= one
        
    for i in range(len(shorter)):
        final.append(one[i])
        final.append(two[i])
        
    final += longer[i+1:]
    return final

x = [1, 2, 3, 4] 
y = ['a', 'b', 'c','d','e','f'] 
print(merge_lists(x, y))

