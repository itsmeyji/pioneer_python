n , k = map(int, input().split())
a = list(map(int,input().split()))

for i in range(1, n):
    for j in range(n-i):
        if a[j]<a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]

print(a[k-1])