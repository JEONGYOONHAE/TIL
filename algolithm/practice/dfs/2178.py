# 2178 미로 턈색
# BFS
from collections import deque

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input())))

# 4방향 (상 우 하 좌)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 방문 기록 표시
visited = [[0] * M for _ in range(N)]

queue = deque([(0, 0)])
visited[0][0] = 1   # 시작점 1

while queue:
    x, y = queue.popleft()

    # 목적지 도착할 경우 도착지점 까지의 길이 출력
    if x == N - 1 and y == M - 1:
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 다음 이동 경로가 범위안에 있는 경우
        if 0 <= nx < N and 0 <= ny < M:
            # 방문기록이 없고 미로에는 길이 존재하는 경우
            if not visited[nx][ny] and arr[nx][ny] == 1:
                # 방문기록 추가
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))