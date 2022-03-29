# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

def baby_gin(player):
    if len(player) < 3:
        return False
    win_check = [0] * 10
    for i in player:
        win_check[i] += 1

    for i in win_check:
        if i >= 3:
            return 1
    idx = 0
    while idx < 8:
        if win_check[idx] and win_check[idx+1] and win_check[idx+2]:
            return 1
        else:
            idx += 1

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    player1 = []
    player2 = []
    winner = 0
    for i in range(0, 12, 2):
        player1.append(arr[i])
        if baby_gin(player1):
            winner = 1
            break

        player2.append(arr[i+1])
        if baby_gin(player2):
            winner = 2
            break
    else:
        winner = 0

    print(f'#{tc} {winner}')
