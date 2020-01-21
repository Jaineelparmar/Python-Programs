def contains(hay, needle):
    for item in hay:
        if item == needle:
            break
        else:
            raise ValueError('Needle not found')

print(contains([23, 'needle', 0xbadc0ffee], 'needle'))
