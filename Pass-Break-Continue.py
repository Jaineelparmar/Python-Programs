#PASS ||  BREAK   || CONTINUE 

li = [1,2,-1,4,5,6]
for i in li:
     if i== -1:
         pass
     else:
         print(i)
print('-'*20)


li = [1,2,3,-1,4,5,6]
for i in li:
     if i== -1:
         break
     else:
         print(i)
     print('hello world')
print('-'*20)



li = [1,2,3,-1,4,5,6]
for i in li:
     if i== -1:
         continue
     else:
         print(i)
     print ('hello world')

print('-'*20)
