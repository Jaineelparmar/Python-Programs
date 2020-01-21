#Given a list of strings print count of strings starting with capital 'U'

li=['abc','Unity','xyz','Ubuntu','pqr','Udacity']
count=0
y = []
for x in li:
    if x[0]=='U' :
        count += 1
        y.append(x)
        
print(count)
print(y)

