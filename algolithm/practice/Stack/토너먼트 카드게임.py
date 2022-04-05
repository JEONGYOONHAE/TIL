# 02/24
# 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
def team(s, e):
    if s == e:
        return s
    else:
        teamA = team(s, (s+e)//2)
        teamB = team((s+e)//2+1, e)
        return winner(teamA, teamB)

def winner(a, b):
    l = cards[a-1]
    r = cards[b-1]
    # 1 : 가위, 2 : 바위, 3 : 보
    if l == 1 and r == 3:
        return a
    elif l == 3 and l == 1:
        return b
    elif l == 1 and r == 2:
        return b
    elif l == 2 and r == 1:
        return a
    elif l == 2 and r == 3:
        return b
    elif l == 3 and r == 2:
        return a
    else:
        return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = team(1, N)
    print(f'#{tc} {result}')