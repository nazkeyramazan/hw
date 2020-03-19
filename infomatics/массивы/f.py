n = int(input())
s = input()

data = s.split()

k = 0

for i in range(n):
    if int(data[i-2]) < int(data[i-1]) and int(data[i]) < int(data[i-1]):
        k += 1

print(k)