for _ in range(10):
    tc, e = map(int, input().split())
    arr = [[0]*100 for _ in range(2)]

    for i in range(e):
        r, c = map(int, input().split())
        arr[r][c] = 1

    stack = []
    visited = []
    result = 0
    while stack:
        top = stack[-1]
        if top == 99:
            result = 1
            break

        for i in range():
            if arr[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
        else:
            stack.pop()

