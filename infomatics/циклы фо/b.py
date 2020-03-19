a = int(input())
b = int(input())
c = int(input())
d = int(input())

answ = []

for i in range(a, b+1):
    if(i%d==c):
        answ.append(i)

print(' '.join(str(i) for i in answ))