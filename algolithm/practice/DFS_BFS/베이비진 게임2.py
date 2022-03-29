# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임(2)

def baby_gin(player):
    # 3 이하일 경우 패스
    if sum(player) < 3:
        return 0
    # 카드의 개수가 3 이상일 경우 triple -> True
    for i in player:
        if i >= 3:
            return 1
    idx = 0
    while idx < 8:  # run 검사
        if player[idx] and player[idx+1] and player[idx+2]:
            return 1
        else:
            idx += 1

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0
    for i in range(0, 12, 2):
        player1[arr[i]] += 1    # 숫자에 해당하는 개수 +1
        if baby_gin(player1):
            winner = 1
            break

        player2[arr[i+1]] += 1
        if baby_gin(player2):
            winner = 2
            break

    print(f'#{tc} {winner}')
