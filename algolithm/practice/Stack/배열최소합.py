# 02/24
# 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
def solve(idx, ssum):  # (방문할 i열, 부분합)
    global mini_sum
    if idx == N:  # 방문할 열이 N배열의 마지막일 경우
        if mini_sum > ssum:  # 최솟값 비교
            mini_sum = ssum
        return
    if ssum > mini_sum:
        return
    for j in range(N):
        if visited[j] == 0:  # 방문한 행이 아닐 경우
            visited[j] = 1  # 방문을 표시
            solve(idx+1, ssum+arr[idx][j])  # 부분합에 해당 행열 값을 더함
            visited[j] = 0  # 방문 표시 해제제

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mini_sum = 100      # 배열 최소합
    visited = [0] * N   # 방문기록
    solve(0, 0)         # (행 0, 부분합 0)
    print(f'#{tc} {mini_sum}')

