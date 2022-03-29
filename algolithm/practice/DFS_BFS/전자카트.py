# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트
def golf(cnt, y, part_sum):
    global result
    if cnt == N:                # 종료조건
        part_sum += arr[y][0]
        if part_sum < result:    # 베터리 소모량 최솟값 갱신
            result = part_sum
            return

    for i in range(1, N):
        if not arr[y][i]:       # 값이 없을 경우 패스
            continue
        if not visited[i]:      # 방문한경우가 아니라면
            visited[i] = 1      # 방문표시
            golf(cnt+1, i, part_sum + arr[y][i])    # 현재 y(열)와 다음 시작하는 i(행)를 동일하게 설정
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 100 * N
    golf(1, 0, 0)   # 처음 시작의 y는 0
    print(f'#{tc} {result}')

