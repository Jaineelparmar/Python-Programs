#to find length of words in a list
def length_of_words(li):
    final = []
    for i in li:
        final.append(len(i))
    return final

x = ['i', 'like', 'python', 'programming']
print(length_of_words(x))