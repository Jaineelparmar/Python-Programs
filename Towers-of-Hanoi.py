#towers of hanoi problem

def towers(n, a, c, b):
    if n == 1:
        print('move disk %i from pole %s to pole %s' %(n, a, c))
    else:
        towers(n-1, a, b, c)
        print('move disk %i from pole %s to pole %s' %(n, a, c))
        towers(n-1, b, c, a)

n = int(input('enter number of diska:'))
towers(n, 'A', 'C', 'B')
