arr = [2, 5, 7, 1, 9, 10, 2, 3, 6]
N = 9
K = 4
result = []
def solve (idx, selected, cnt):
    global result
    if cnt == K :
        for i in range(len(selected)):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return
    if idx == N :
        return

    selected[idx] = 1
    solve(idx+1, selected, cnt+1)

    selected[idx] = 0
    solve(idx + 1, selected, cnt)

solve(0,[0]*N,0)