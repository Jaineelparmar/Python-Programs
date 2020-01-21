#(35th program) -
#IMPLEMENT THE 'GUESS THE NUMBER' GAME IN PYTHON.YOU WILL FIRST SET A PARTICULAR INTEGER AS FINAL ANSWER.IF THE GUESS OF THE USER IS LESS THAN FINAL ANWSER , 
#PRINT 'YOUR GUESS WAS LESS THAN THE ANWSER'  AND TAKE INPUT FROM USER AGAIN. SIMILARLY, DO THE SAME IF THE GUESS IS GREATER THAN ANWSER.IF THE GUESS IS CORRECT, 
#PRINT 'YOUR GUESS IS CORRECT' AND STOP THE PROGRAM. YOUR PROGRAM SHOULD KEEP ON ASKING USER FOR HIS GUESS AS LONG AS HE DOESN'T GET THE GUESS RIGHT.

def guess_the_number(a):
    x = int(input('enter a number:'))
    if a > x :
        return 'Your guess is less than', + a
    elif a < x :
        return 'Your guess is greater than',+ a
    else :
        return 'Your guess is correct'
z = 50
print(guess_the_number(z))
