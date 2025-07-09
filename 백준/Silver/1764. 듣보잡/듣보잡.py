n, m = map(int, input().split())

a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

res = sorted(a & b)

print(len(res))

for i in res:
    print(i)


