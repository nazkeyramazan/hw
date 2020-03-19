n = input()
s = input()

data = s.split()

temp = int(data[0])
b = False
for i in range(len(data)):
    if(temp < 0 and int(data[i]) < 0):
        b = True
    else:
        b = False
        temp=int(data[i])

if b == True:
    print("YES")
else:
    print("NO")