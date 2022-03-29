# 03/25 [모의 SW 역량테스트] 디저트 카페
def DFS(n, ci, cj, v, cnt):
    global si, sj, ans
    if n > 3:
        return
    if n == 3 and ci == si and ans < cnt:
        ans = cnt
        return
    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            DFS(k, ni, nj, v, cnt+1)
            v.pop()

di, dj = (1, 1, -1, -1, 1), (-1, 1, 1, -1, -1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range (N)]
    ans = -1
    for si in range(0, N-2):
        for sj in range(1, N-1):
            DFS(0, si, sj, [], 0)
    print(f'#{tc} {ans}')
