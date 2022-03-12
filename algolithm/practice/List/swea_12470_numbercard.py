# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력
T = int(input())
for tc in range(1, T+1):
    n, card = map(str, input())
    cd = {}
    for c in card:
        cd['c'] += 1


