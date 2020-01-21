'''
GIVEN A PATTERN AND A STRING STR, FIND IF STR FOLLOWS THE SAME PATTERN.
HERE FOLLOW MEANS A FULL MATCH, SUCH THAT THERE IS A BIJECTION BETWEEN A LETTER IN PATTERN AND A NON-EMPTY WORD IN STR.
EX.1 :
I/P : pattern = "abba" , str = "dog cat cat dog"
O/P : TRUE
EX.2 :
I/P : pattern = "abba" , str = "dog cat cat fish"
O/P : FALSE
EX.3 :
I/P : pattern = "aaaa" , str = "dog cat cat dog"
O/P : FALSE
EX.4 :
I/P : pattern = "abba" , str = "dog dog dog dog"
O/P : FALSE
NOTES :
YOU MAY ASSUME PATTERN CONTAINS ONLY LOWERCASE LETTERS , AND STR CONTAINS LOWER LETTERS THAT MAY BE SEPARATED BY A SINGLE SPACE.
'''

class Solution:
    def wordpattern(self, pattern, str):
        words_list = str.split(' ')
        if len(pattern) == len(words_list):
            di = {}
            factored_words = []
            for i in range(len(words_list)):
                if words_list[i] not in factored_words:
                    di[pattern[i]] = words_list[i]
                factored_words.append(words_list[i])
            final = ''
            for char in pattern:
                final += di[char]+' ' if char in di else ''
            return str == final[:-1]
        else:
            return False

sol = Solution()
print(sol.wordpattern('abba','dog cat cat dog'))    # output = true.
print(sol.wordpattern('abba','dog cat cat fish'))    # output = false.
print(sol.wordpattern('aaaa','dog cat cat dog'))    # output = false.
print(sol.wordpattern('abba','dog dog dog dog'))    # output = false.
