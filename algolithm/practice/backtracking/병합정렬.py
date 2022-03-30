# (재귀) 배열을 계속 반으로 나눈다. 0~mid 전까지 : left배열 / mid ~ last 까지 : right 배열
# 배열의 길이가 1일 때, 배열을 리턴
# 배열의 길이가 2 이상일 때, left 배열과 right 배열을 정렬하면서 합친다.
# 각 부분배열의 첫번째 인덱스부터 비교한다. 더 작은 값을 배열에 넣는다. (만약 값이 같으면 왼쪽 배열의 값을 넣는다. 왼쪽 배열의 원소가 오른쪽 배열의 원소보다 클 때만 오른쪽 배열의 원소를 넣고, 그렇게 해야 마지막 원소 비교할 때 올바르게 카운팅을 할 수 있기 때문이다.)
# 두 부분배열 중 하나가 탐색이 끝나면 나머지 한 배열의 나머지 값들을 순서대로 배열에 넣는다.
# 합쳐진 배열을 리턴한다.

def merge_arr(l, r):
    global result   # 왼쪽 원소가 오른쪽 원소보다 큰 경우 += 1
    if l[-1] > r[-1]:
        result += 1
    marr = []   # 정렬된 arr을 받을 리스트
    li, ri = 0, 0
    L = len(l)
    R = len(r)

    while li < L and ri < R:    # l, r 서로의 범위안에 해당할 경우
        if l[li] <= r[ri]:
            marr.append(l[li])
            li += 1
        else:
            marr.append(r[ri])
            ri += 1
    if li != L: # 왼쪽 리스트에 값이 있을 경우
        marr += l[li:]
    if ri != R: # 오른쪽 리스트에 값이 남아있을 경우
        marr += r[ri:]
    return marr

def merge_sort(arr):
    if len(arr) == 1:   # 길이가 1 이면 그대로 반환
        return arr
    m = len(arr) // 2           # 왼쪽점과 오른쪽점을 지정하면서 분할과 병합을 반복
    l = merge_sort(arr[:m])     # 왼쪽 배열 인덱스
    r = merge_sort(arr[m:])     # 오른쪽 배열 인덱스
    return merge_arr(l, r)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    answer = merge_sort(arr)
    print(f'#{tc} {answer[N//2]} {result}')


