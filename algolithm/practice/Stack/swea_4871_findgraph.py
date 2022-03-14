T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s, e = map(int, input().split())
        arr[s][e] = 1

    # S에서 G까지 가는 경로가 있는가
    S, G = map(int, input().split())
    visited = [0]*(V+1)
    stack = []
    stack.append(S)
    visited[S] = 1

    # dfs 시작
    result = 0
    while stack:
        top = stack[-1]
        if top == G:
            result = 1
            break
        for i in range(V+1):
            if arr[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    print(f'#{tc} {result}')
