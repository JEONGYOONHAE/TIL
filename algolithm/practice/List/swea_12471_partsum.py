# 구간 합 구하기
# n 길이만큼의 숫자 리스트에서 m길이의 구간 합 구하기
# 구간합 중 최대값과 최소값 차이 구하기
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    mysum = 0
    sumli = []
    for i in range(n-m):
        for j in range(m):
            mysum += arr[i+j]
        sumli.append(mysum)

    print(f'#{tc} {max(sumli) - min(sumli)}')

