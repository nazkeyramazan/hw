n = input()
s = input()

ans = 0
for el in s.split():
    if int(el) > 0:
        ans +=1

print(ans)