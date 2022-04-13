from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    INF = float('inf')
    distance = [[INF for _ in range(N)] for _ in range(N)]
    distance[0][0] = 0
    queue = deque()
    queue.append((0, 0))
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            ny, nx = dy + y, dx + x
            if 0 <= ny < N and 0 <= nx < N:
                temp = 1
                if map_list[ny][nx] > map_list[y][x]:
                    temp += map_list[ny][nx] - map_list[y][x]
                if distance[ny][nx] > distance[y][x] + temp:
                    distance[ny][nx] = distance[y][x] + temp
                    queue.append((ny, nx))
    result = distance[N - 1][N - 1]
    print(f'#{tc} {result}')