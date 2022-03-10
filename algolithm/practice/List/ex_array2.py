# 5X5 배열
arr = [[] for _ in range(5)]

# 시계방향 회전
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

sum = 0
for i in range(5):
    for j in range(5):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 5 and 0 <= nj < 5:         # 이웃한 값이 배열의 범위내에 존재할 경우
                sum += abs(arr[ni][nj]-arr[i][j])   # 절댓값을 구함
            else:                                   # 배열 범위에 없을 경우
                sum += 0                            # 0을 더함 / continue

print(sum)