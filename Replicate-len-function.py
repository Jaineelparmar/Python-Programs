#Replicate the working of len function.

str = 'python'
print(len(str))

#We can replicate len function using another variable by assigning it zero

str = 'python'
x = 0
for i in str:
    x += 1
print(x)
