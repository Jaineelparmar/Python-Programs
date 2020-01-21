#BUBBLE SORT
def bubble(li):
    for i in range(len(li)-1, 0, -1):
        for j in range(i):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
x = [64, 34, 25, 12, 22, 11, 90]
bubble(x)
print(x)

  