#To check if the string starts with a vowel.

s1='jaineel'
if s1[0]=='a' or s1[0]=='e' or s1[0]=='i' or s1[0]=='o' or s1[0]=='u' :
    print(s1+',starts with vowels')
else :
    print(s1+",doesn't starts with vowels")

########################################
#USING IN OPERATOR

s1='amanda'
vowels=('a','e','i','o','u') 
#or we can also use vowels = 'aeiou'

if s1[0] in vowels :
    print(s1+',starts with vowels')
else :
    print(s1+",doesn't starts with vowels")



#Count of vowels from a list.

def count_of_vowels(li):
    count = 0
    for i in li:
        if i[0] in ('a', 'e', 'i', 'o', 'u'):
            count += 1
    return count
x = ['abc', 'ufg', 'fgs', 'greg', 'ifd']
print(count_of_vowels(x))


