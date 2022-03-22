# 0 ~ 9 사이의 숫자 카드에서 임의로 카드 6장을 뽑았을 때,
# 3장의 카드가 연속적인 번호를 갖는 경우 run,
# 3장의 카드가 동일한 번호를 갖는 경우 triplet
# run과 triplet로만 구성된 경우 baby-gin

# 완전탐색
# 예시 : 2 7 3 4 7 7
arr = [2, 7, 3, 4, 7, 7]
N = 6
def check_baby():
    for i in range(N):  # 첫번째 인덱스
        for j in range(N):  # 두번째 인덱스
            if i == j:      # 첫번째 인덱스와 같지 않으면 입력
                continue
            else:
                for k in range(N):  # 세번째 인덱스
                    if i == k and j == k:   # 첫번째, 두번째 인덱스와 같지 않으면 입력
                        continue
                    else:
                        # i, j, k 가 다 다름
                        for a in range(N):  # 네번째 인덱스
                            if a == i or a == j or a == k:  # 1~3 인덱스와 같지 않으면 입력
                                continue
                            for b in range(N):  # 다섯번째 인덱스
                                if b == i or b == j or b == k or b == a:    # 1~4 인덱스와 같지 않으면 입력
                                    continue
                                for c in range(N):  # 여섯번째 인덱스
                                    if c == i or c == j or c == k or c == a or c == b:  # 1~5 인덱스와 같지 않으면 입력
                                        continue
                                    # arr[i], arr[j], arr[k], arr[a], arr[b], arr[c] 순서
                                    result = 0  # run / triplet 여부 카운트
                                    # arr[i], arr[j], arr[k] run, triplet 검사
                                    if arr[i]+1 == arr[j] and arr[i]+2 == arr[k]:
                                        result += 1
                                    elif arr[i] == arr[j] and arr[i] == arr[k]:
                                        result += 1
                                    # arr[a], arr[b], arr[c] run, triplet 검사
                                    if arr[a]+1 == arr[b] and arr[a]+2 == arr[c]:
                                        result += 1
                                    elif arr[a] == arr[b] and arr[a] == arr[c]:
                                        result += 1
                                    # result == 2 -> True
                                    if result == 2:
                                        return True
    # return 문을 만나지 못할 경우 False
    return False

result = check_baby()
if result:
    print('baby_gin!!!')
else:
    print('nope')
