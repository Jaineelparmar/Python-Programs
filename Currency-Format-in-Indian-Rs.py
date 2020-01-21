#CURRENCY Format in  Indian Rs.

def currency(x):
    y = ' '
    if len(x) > 3:
        a = ','+ str(x[-3:])
    else:
        a = x
    
    b = (x[:-3])
    c = 0
    for i in b[::-1]:
        c += 1
        y = y+str(i)
        if c == 2:
            c = 0
            y = y + ','
    y = y[::-1]
    Y = y + a
    return Y
z = str(int(input('Enter the amount:')))
print(currency(z))
