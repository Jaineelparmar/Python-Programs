'''
Data Structure includes ID, Marks, Subjects.
-How much did student with ID 2 scored in Maths.
-Aggregate score of each Student.
'''


#Dictionary inside another Dictionary
di={1:{'physics':45,'maths':90,'english':81,'chemistry':71,'biology':65},
    2:{'physics':46,'maths':91,'english':82,'chemistry':72,'biology':65},
    3:{'physics':47,'maths':92,'english':83,'chemistry':73,'biology':65},
    4:{'physics':48,'maths':93,'english':84,'chemistry':74,'biology':65},
    5:{'physics':49,'maths':94,'english':85,'chemistry':75,'biology':65}}

#Print Score of Maths for Student ID = 2
print('Student ID 2 scored {} marks out of 100 in Maths'.format(str(di[2]['maths'])))

#Print Average for Student ID = 1
one = di[1]['physics']+di[1]['maths']+di[1]['english']+di[1]['chemistry']+di[1]['biology']
print('Average score for student ID 1 is = '+str(one/5)+' %')

#Print Average for Student ID = 2
two = di[2]['physics']+di[2]['maths']+di[2]['english']+di[2]['chemistry']+di[2]['biology']
print('Average score for student ID 2 is = '+str(two/5)+' %')

#Print Average for Student ID = 3
three = di[3]['physics']+di[3]['maths']+di[3]['english']+di[3]['chemistry']+di[3]['biology']
print('Average score for student ID 3 is = '+str(three/5)+' %')

#Print Average for Student ID = 4
four = di[4]['physics']+di[4]['maths']+di[4]['english']+di[4]['chemistry']+di[4]['biology']
print('Average score for student ID 4 is = '+str(four/5)+' %')

#Print Average for Student ID = 5
five = di[5]['physics']+di[5]['maths']+di[5]['english']+di[5]['chemistry']+di[5]['biology']
print('Average score for student ID 5 is = '+str(five/5)+' %')