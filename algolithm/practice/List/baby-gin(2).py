# 탐욕 알고리즘으로 baby-gin game

# 현재에서 최적인 경우를 찾아 나가는 방법
arr = [2, 7, 3, 4, 7, 7]
N = 6
cnt_arr = [0]*10
# 1. 배열의 숫자를 카운트
# 0 보다 크다는 의미는 해당 숫자의 카드가 있다는 말
for i in range(N):
    cnt_arr[arr[i]] += 1
# print(cnt_arr)

for i in range(len(cnt_arr)):
    # 2. 카운트된 배열에서 3 이상일 경우 triplet
    if cnt_arr[i] >= 3:
        cnt_arr[i] -= 3 # 카운트가 겹치지 않게 -3 해줌
    elif cnt_arr[i] > 0:
        # 각 숫자 인덱스의 값이 있으면 run
        # 교수님 코드에서는 cnt_arr[i] == cnt_arr[i+1] and cnt_arr[i] == cnt_arr[i+2] 로 조건이 되어있어서 헷갈렸음
        # cnt_arr은 카운트가 된 배열이기 때문에 숫자카드의 개수가 같은게 아니라 카드의 유무 여부가 일치해야한다고 생각함
        if cnt_arr[i] and cnt_arr[i+1] and cnt_arr[i+2]:
            cnt_arr[i] -= 1     # 카운트 중복되지 않도록 -1
            cnt_arr[i+1] -= 1
            cnt_arr[i+2] -= 1
            continue

if sum(cnt_arr) == 0:
    print('baby-gin')
else:
    print('nope')
