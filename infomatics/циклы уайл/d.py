n = int(input())
b = 0
while n:
    b += n%2
    n /= 2
if b ==1:
    print('YES')
else:
    print('NO')