#A program is a sentence that contains all letters of english alphabet at least once:
# 'the quick brown fox jumps over lazy dog' 
#Your task here is to write a function to check a sentence to see if it is a pangram or not.
       
       
def pangram_or_not(a):
    final = 'abcdefghijklmnopqrstuvwxyz'
    for ch in final:
        if ch not in a:
            return False
        else:
            return True
x = 'the quick brown fox jumps over the lazy dog 12345'
if(pangram_or_not(x) == True): 
    print("pangram") 
else: 
    print("Not a pangram") 
