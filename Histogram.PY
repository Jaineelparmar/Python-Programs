# a histogram() that takes a list of integers and prints a histogram to the screen. For example,histogram([4, 9, 7]) should print the following:
#**** = 4 stars

def histogram(li):
    for i in li:
        output = ''
        x = i 
        while (x > 0):
            output += '*'
            x = x-1
        print(output)

histogram([1, 2, 3, 4, 5])

#OR

def histogram(li):
    for i in li:
        print('*'*i)
        
x = [1, 2, 3, 4, 5]
histogram(x)