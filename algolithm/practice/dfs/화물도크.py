# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])
    cnt = 1
    end = arr[0][1]
    for i in range(1, N):
        if end <= arr[i][0]:
            cnt += 1
            end = arr[i][1]
    print(f'#{tc} {cnt}')