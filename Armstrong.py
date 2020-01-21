def armstrong_or_not(a):
    sum = 0
    temp = a
    while temp > 0:
        digit = temp%10
        sum += digit**3
        temp //= 10
    if a == sum:
        return str(a)+' is an armstrong number'
    else:
        return str(a)+' is not an armstrong number'

x = int(input('Enter a number:'))
print(armstrong_or_not(x))