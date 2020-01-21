#PASSING A GROUP OF ELEMENTS TO A FUNCTION

#to accept group of numbers and find their average

def calculate(lst):
    n = len(lst)
    sum = 0
    for i in lst:
        sum += i
        avg = sum/n
    return sum,avg 

print('enter numbers separated by space: ')
lst = [int(x) for x in input().split()]

x, y = calculate(lst)
print('total:',x)
print('average:',y)



#to accept group of strings and display

def display(lst):
    for i in lst:
        print(i)

print('enter strings separated by comma: ')
lst = [x for x in input().split(',')]
    
display(lst)