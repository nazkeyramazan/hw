n = int(input())
s = input()

data = s.split()

ans = ''

for el in data[::2]:
    ans += el + ' '

print(ans)