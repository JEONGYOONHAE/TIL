# 02/22
# [S/W 문제해결 기본] 4일차 - 길찾기

for _ in range(1, 11):
    # test case, 길의 총 개수
    tc, v = map(int, input().split())
    # 간선정보를 리스트로 입력받음
    lst = list(map(int, input().split()))
    # 간선정보를 노드별로 입력할 리스트
    arr = [[0]*100 for _ in range(2)]
    for i in range(0, v*2, 2):
        v = lst[i]
        e = lst[i+1]
        if not arr[v][0]:
            arr[v][0] = e
        else:
            arr[v][1] = e

    stack = []
    visited = [0] * 100
    stack.append(0)
    visited[0] = 1
    answer = 0
    while stack:
        now = stack[-1]
        for i in arr[now]:
            if i == 99:
                answer = 1
                break
            if not visited[i]:
                stack.append(i)
                visited[i] = 1

    print(f'#{tc} {answer}')