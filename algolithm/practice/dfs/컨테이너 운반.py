# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
def solve(ssum):
    global result
    if result < ssum:   # 화물 적재 최대값 갱신
        result = ssum
    for i in range(M):
        for j in range(N):
            # 화물의 크기가 트럭의 적재용량 범위에 있고 출발한 적이 없는 경우
            if t[i] >= w[j] and not t_used[i] and not w_used[j] :
                w_used[j] = 1
                t_used[i] = 1
                solve(ssum + w[j])

T  = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 컨테이너 수 N, 트럭 수 M
    w = list(map(int,input().split()))  # N개 화물의 무게
    t = list(map(int,input().split()))  # 트럭의 적재용량
    result = 0  # 컨테이너 최대 용량
    w.sort(reverse=True)    # 오름차순 정렬 (큰 화물부터)
    t.sort(reverse=True)
    t_used = [0] * M     # 출발한 트럭인지 확인
    w_used = [0] * N     # 적재한 컨테이너인지 확인
    solve(0)
    print(f'#{tc} {result}')
