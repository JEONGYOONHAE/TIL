# 달팽이 배열

# 5x5 2차원 배열 생성
arr = [[0]*5 for _ in range(5)]

# while 문을 이용
# 배열을 진행하면서 벽에 부딪힐 경우 방향 전환
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
i = 0
j = 0
d = 0   # 이동방향 리스트 인덱스
# arr[0][0] = 1
k = 1   # 배열 안에 입력할 숫자 (1 ~ 25)
while k < 26:
    # ni, nj가 배열의 범위 안에 있고, arr[ni][nj]의 위치에 이전에 입력한 값이 없어야함(중복으로 입력되지 않기 위해)
    if 0 <= i < 5 and 0 <= j < 5 and arr[i][j] == 0:
        arr[i][j] = k
        k += 1
    else:
        i -= di[d]
        j -= dj[d]
        d = (d + 1) % 4

    i += di[d]
    j += dj[d]

for i in range(5):
    for j in range(5):
        print(arr[i][j], end=' ')
    print()