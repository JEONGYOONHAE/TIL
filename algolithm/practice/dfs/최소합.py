# 5188. [파이썬 S/W 문제해결 구현] 2일차 - 최소합
def DFS(si, sj):
    global result, part_sum
    if si == N-1 and sj == N-1:     # 도착한 경우
        if part_sum < result:       # 최소값을 저장
            result = part_sum
            return
    if result < part_sum:
        return

    di = [0, 1]
    dj = [1, 0]
    for d in range(2):              # 두 방향으로 이동하며 검색
        ni = si + di[d]             # 다음 좌표
        nj = sj + dj[d]
        if ni < 0 or ni > N-1 or nj < 0 or nj > N-1:    # 다음 좌표가 범위를 넘어가면 continue
            continue
        # 다음 좌표가 범위 안에 있고 방문한 적이 없는 경우
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            part_sum += arr[ni][nj]
            DFS(ni, nj)
            part_sum -= arr[ni][nj]
            visited[ni][nj] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    result = 10 * 2 * N
    part_sum = arr[0][0]
    DFS(0, 0)

    print(f'#{tc} {result}')