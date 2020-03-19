n = int(input())

s = input()

ans =''
for el in s.split():
    if(int(el)%2==0):
        ans += el+' '

print(ans)