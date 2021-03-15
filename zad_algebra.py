from math import *

a = 4.8
b = 2
n = 2

m = 0

if n <= b:
    print("n <= b")
    m = (n + a / -b) #+ sqrt(sin(pow(a, 2)) - cos(n))
elif n == b:
    print("n == b")
    m = pow(b, 2) + tan(n * a)

if n > b:
    print("n > b")
    m = pow(b, 3) + n * pow(a, 2)

print("m:", m)
