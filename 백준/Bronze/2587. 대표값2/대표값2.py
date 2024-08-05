a = [int(input()) for i in range(5)]

for i in range(1, len(a)-1):
    for j in range(0, len(a)-i):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp


print(int(sum(a)/len(a)))
print(a[2])