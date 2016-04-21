def max_number (L):
    max_value = L[0]
    for n in L:
        if n > max_value:
            max_value = n
    return max_value

L = [0. -2, 100, 200, 4]

print 'max: ', max_number(L)




