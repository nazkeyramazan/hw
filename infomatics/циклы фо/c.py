from math import ceil, sqrt

a = int(input())
b = int(input())

for i in range(ceil(sqrt(a)), ceil(sqrt(b))):
    print(i*i)