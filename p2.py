def cubic(x):
    result = x * x * x
    return result

def cubic2(x):
    y = 20
    return x * x * x
def adder (n1, n2):
    return n1+n2

def avg_three (n1,n2,n3):
    temp = n1+n2+n3
    return temp/3.0

x = 100

value1 = cubic(3)

value2 = cubic2(3)
print "x -", x
print "Value 1 - ", value1
print "value 2 - ", value2

print "added - ", adder(10,1)

print "Avg 18, 23, 19 -", avg_three(18, 23, 19)
print "Avg 34, 31, 128 -", avg_three(34, 31, 128)

