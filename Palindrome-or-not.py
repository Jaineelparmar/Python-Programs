#palindrome or not

def palindrome_or_not(a):
    if a==a[::-1]:
        return str(a)+" is a Palindrome"
    else:
        return str(a)+" is not a Palindrome"

x=input("enter sequence:")
print(palindrome_or_not(x))
