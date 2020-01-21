#SUM OF NUMBERS IN A LIST USING RECURSION.

def sum_of_numbers(li):
    if len(li) == 1:
        return li[0]
    else:
        sum = li[0]+sum_of_numbers(li[1:])
        return sum
x = [1, 2, 3, 4, 5, 6]
print(sum_of_numbers(x))