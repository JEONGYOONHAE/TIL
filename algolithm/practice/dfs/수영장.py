# 03/25 [모의 SW 역량테스트] 수영장
def DFS(n, ssum):
    global ans
    if n > 12:
        if ans > ssum:
            ans = ssum
        return
    # 일일권
    DFS(n+1, ssum + use[n]*day)
    # 월간
    DFS(n+1, ssum + mon)
    # 3개월
    DFS(n+3, ssum + mon3)
    # 년간
    DFS(n+12, ssum + year)

T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    use = [0]+list(map(int, input().split()))
    ans = 123457898
    ssum = 0
    DFS(1, 0)
    print(f'#{tc} {ans}')
