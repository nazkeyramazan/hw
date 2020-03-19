n = input()
s = input()

data = s.split()

temp = int(data[0])
k = 0
for i in range(len(data)):
    if temp < int(data[i]):
        temp = int(data[i])
        k += 1

print(k)