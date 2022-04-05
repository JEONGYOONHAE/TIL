# 02/24
# 4875. [파이썬 S/W 문제해결 기본] 5일차 - 미로

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().rstrip('\r'))) for _ in range(N)]
    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break
    result = 0
    stack = []                          # 방문할 수 있는 길을 담아둠
    stack.append((si, sj))              # si, sj로 시작하기 때문에 추가
    visited = [[0]*N for _ in range(N)] # 방문여부 표시
    visited[si][sj] = 1                 # si, sj 방문 표시
    # 길찾기 시작
    while stack:                        # 방문할 수 있는 길이 있을 경우 실행
        ci, cj = stack[-1]              # 현재위치
        if arr[ci][cj] == 3:            # 도착지점(3)에 도착할 경우
            result = 1                  # True & break
            break
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]    # 상하좌우 네방향
        for di, dj in dir:
            ni = ci + di    # 전진할 위치
            nj = cj + dj
            # 전진할 위치가 배열의 범위안에 있고, 방문기록이 없으며 벽이 아닌경우 (arr[ni][nj] == 0 으로 조건을 만들면 도착지점으로도 못감)
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 1:
                visited[ni][nj] = 1         # 방문기록을 표시하고
                stack.append((ni, nj))      # 갈수 있는 길 목록에도 추가
                break
        else:           # 네 방향을 다돌아도 갈 수 있는 길이 없을경우
            stack.pop() # 뒤로 돌아감

    print(f'#{tc} {result}')


