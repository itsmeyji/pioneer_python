n = int(input())

l = [int(input()) for _ in range(n)]

l.sort(reverse=True)

for i in range (0, n):
    print(l[i])
    
#입력 형식이 int로 되도록 주의