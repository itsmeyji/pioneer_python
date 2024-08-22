import sys

stack = []

n = int(input())

for _ in range(n):
    li = sys.stdin.readline().split()

    if li[0] == "1":
        stack.append(int(li[1]))

    elif li[0] == "2":
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif li[0] == "3":
        print(len(stack))

    elif li[0] == "4":
        if stack :
            print(0)
        else:
            print(1)

    elif li[0] == "5":
        if stack :
            print(stack[-1])
        else:
            print(-1)