# 달팽이 배열

# 5x5 2차원 배열 생성
arr = [[0]*5 for _ in range(5)]

# while 문을 이용
# 배열을 진행하면서 벽에 부딪힐 경우 방향 전환
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
k = 1   # 배열 안에 입력할 숫자 (1 ~ 25)
i = 0
j = 0
while True:
    if 0 <= i < 5 and 0 <= j < 5 and arr[i][j] == 0:
        arr[i][j] = k
    else:
