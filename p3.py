from math import sqrt
def find_hypotenuse(a,b):
    a_squared = a*a
    b_squared = b*b
    result = sqrt(a_squared + b_squared)
    return result

print "hypotenuse 3, 4 - ", find_hypotenuse(3,4)

def print_name(name):
    print 'Person name:' + name
    return

print_name('Jose')
print_name('Ned')





