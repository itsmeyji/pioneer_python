n = int(input())

l = list(map(int, input().split()))
l.sort()

time = []
s = 0

for i in range (n):
    s += l[i]
    time.append(s)

print(sum(time))
