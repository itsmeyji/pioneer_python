num = input()
a = [int(char) for char in num]



for i in range(len(a)):
    max_i = i
    for j in range(i+1, len(a)):
        if a[j]>a[max_i] :
            max_i = j
    a[max_i], a[i] = a[i], a[max_i]

for k in range(len(a)):
    print(a[k], end ='')