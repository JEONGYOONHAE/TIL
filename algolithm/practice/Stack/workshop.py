import sys

sys.stdin = open('input.txt')

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# dfs
def dfs(y, x):
    global result
    if arr[y][x] == 3 :   # 도착지점에 도착하면 1을 반환
        result = 1
        return
    for i, j in dir:    # 4방향을 도는 반복문 실행
        ny = y + i
        nx = x + j

        if arr[ny][nx] != 1:    # 벽이 아니라면
            arr[y][x] = 1       # 현재위치를 벽으로 체크
            dfs(ny, nx)         # 재귀호출

for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    result = 0
    dfs(1,1)
    print(f'#{tc} {result}')


