# 부분집합
def solve(idx, selected):
    global min_result
    if idx == N:
        group1 = []
        group2 = []
        for i in range(N):
            if selected[i]: # 0이 아니면 group1에 추가
                group1.append(arr[i])
            else:
                group2.append(arr[i])

        work1 = sum(group1)
        work2 = sum(group2)
        result = abs(work1 - work2)
        if result < min_result:
            min_result = result
        return
    else:
        selected[idx] = 0
        solve(idx+1, selected)

        selected[idx] = 1
        solve(idx+1, selected)

min_result = 0xfffff
arr = [2, 5, 7, 1, 9, 10, 2, 3, 6]
N = 9
selected = [0] * N
solve(0,selected)
print(min_result)