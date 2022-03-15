edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
V = 7
adj = [[0]*(V+1) for _ in range(V+1)]
for i in range(0, len(edges), 2):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs():
    stack = []
    visited = [0] * (V+1)
    stack.append(1)
    visited[1] = 1
    print(1, end=' ')
    while stack:
        top = stack[-1]
        for i in range(V+1):
            if adj[top][i] and not visited[i]:
                print(i, end=' ')
                visited[i] = 1
                stack.append(i)
                break
        else:
            stack.pop()