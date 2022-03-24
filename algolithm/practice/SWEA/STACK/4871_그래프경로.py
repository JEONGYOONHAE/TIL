T = int(input())
for tc in range(1, T+1):
    # V개 노드, E개 간선
    V, E = map(int, input().split())
    # 간선정보를 입력할 2차원 배열
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1

    # 출발 노드 S, 도착 노드 G
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    stack = []
    stack.append(S)     # start 값 추가
    visited[S] = 1      # S를 방문하므로 1
    result = 0          # 0으로 설정
    while stack:
        top = stack[-1]
        if top == G:
            result = 1
            break
        for i in range(V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()
    print(f'#{tc} {result}')

