n = int(input())

honeycomb = 1  # 시작 벌집 개수
cnt = 1
while n > honeycomb :
    honeycomb += 6 * cnt  # 벌집 증가 넘버링 : n + 6 * 겹수
    cnt += 1  # 중앙으로부터 거리
    
print(cnt)