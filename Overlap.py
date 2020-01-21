# a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.
def overlap(a,b):
    a= set(x)
    b= set(y)
    if (a&b):
        return True
    else:
        return False
x = [1, 2, 3, 4, 5]
y = [6, 7, 8]    
print(overlap(x,y))