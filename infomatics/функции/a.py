def min(a,b,c,d):

    if(a<=b and a<=c and a<=d):
        return a

    if (b <= a and b <= c and b <= d):
        return b

    if (c <= a and c <= b and c <= d):
        return c

    if (d <= b and d <= c and d <= c):
        return d


x =int(input())
y =int(input())
z =int(input())
m =int(input())
print(min(x , y, z, m))