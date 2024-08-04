n = int(input())
a = []

for _ in range(n):
    a.append(int(input()))

for i in range(len(a) - 1):
    for j in range(len(a) - 1):
        if a[j] > a[j + 1]: #만약 앞의 원소가 뒤의 원소보다 크다면
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp

for i in range(len(a)):
    print(a[i])