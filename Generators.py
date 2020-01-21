###################### GENERATORS #################################

# generators return a sequence of values.It uses 'yield' statement this statement is useful to return value.

#RETURNS SEQUENCE OF NUMBER FROM x TO y

def mygen(x, y):
    while x<=y:
        yield x
        x += 1
g = mygen(5, 10)

for i in g:
    print(i,'\n')


#RETURNS CHARACTERS FROM A TO C

def mygen():
    yield 'A'
    yield 'B'
    yield 'C'

g = mygen()

print(next(g))                  #display A
print(next(g))                  #display B
print(next(g))                  #display C
print(next(g))                  #error
