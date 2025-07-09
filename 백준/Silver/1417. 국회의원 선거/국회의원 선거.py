n = int(input())
can_list = list()
cnt = 0

# 입력 받기
for i in range(n) :
    temp = int(input())
    can_list.append(temp)

# 다솜이 확보 수
pos = can_list[0]

# 다솜 제외 배열
neg_list = list()
neg_list = can_list[1:]

# 다솜이 매수 과정
if (n == 1) :
    cnt = 0
else :
    while True :
        neg_list.sort(reverse=True)
        if ( pos <= neg_list[0]) :
            neg_list[0] -= 1
            pos += 1
            cnt += 1
        else :
            break

print(cnt)