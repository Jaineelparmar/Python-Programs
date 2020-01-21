#aaaabbbabaaabccc => abababc

def alphabets(a):                                                                   
    final = a[0]
    total = a[0]
    for i in a[1:] :
        if i not in final:              
            total = total+i
            final = i
    return total

x = 'aaaabbbabaaabccc'
print(alphabets(x))


#redundant === aaaabbbabaaabccc => abc

def alphabets(a):                                                                   
    final = a[0]
    total = a[0]
    for i in a[1:] :
        if i not in final:              
            total = total+i
            final = final+i
    return total

x = 'aaaabbbabaaabccc'
print(alphabets(x))

#OR

def alphabets(s):
    final=''
    for char in s:
        if char not in final:
            final += char
    return final

x = 'aaaabbbabaaabccc'
print(alphabets(x))

