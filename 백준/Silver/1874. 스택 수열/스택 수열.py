import sys


n = int(sys.stdin.readline())
stack = []
res = []
cnt = 1
temp = 0

for i in range(n):

    num = int(sys.stdin.readline())
    while num >= cnt:
        stack.append(cnt)
        res.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        res.append("-")
    else:
        temp = 1
        break

if temp:
    print("NO")
else:
    for i in res:
        print(i)