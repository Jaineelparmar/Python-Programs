#Count of string into a dictionary aaaabbbabaaabccc => {a:8,b:5,c:3}

def alphabets(a):
    di = {}
    for i in a:
        if i in di:               
            di[i] += 1
        else:
            di[i] = 1

    return di
  
x = 'aaaabbbabaaabccc'
print(alphabets(x))


