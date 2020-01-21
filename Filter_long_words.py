#A function to filter _long_words that takes a list of words that are longer than n.

def filter_long_words(li):
    count = 4
    final = []
    for i in li:
        if len(i) > count:
            final.append(i)
    return final
            
x = ['abc','python','pqr','programming','edece']
print(filter_long_words(x))



# find_longest_word that takes a list of words and returns the length of the longest one.

li=['hi','hello','wonderful']
longest=li[0]
for elem in li[1:]:
    if len(elem)>len(longest):
        longest=elem

x = longest, len(longest)        
print(tuple(x))
