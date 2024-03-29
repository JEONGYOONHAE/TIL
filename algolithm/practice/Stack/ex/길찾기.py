decode = {'112': 0, '122': 1, '221': 2, '114': 3,
          '231': 4, '132': 5, '411': 6, '213': 7,
          '312': 8, '211': 9}
dic = {'0': '0000', '1': '0001', '2': '0010',
       '3': '0011', '4': '0100', '5': '0101',
       '6': '0110', '7': '0111', '8': '1000',
       '9': '1001', 'A': '1010', 'B': '1011',
       'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]
    bl = [''] * N
    for i in range(N):
        for j in range(M):
            bl[i] += dic[arr[i][j]]
    result = []
    visited = []
    ans = 0
    for y in range(N):
        a = b = c = 0
        for x in range(M * 4 - 1, -1, -1):
            if b == 0 and c == 0 and bl[y][x] == '1':
                a += 1
            elif a > 0 and c == 0 and bl[y][x] == '0':
                b += 1
            elif a > 0 and b > 0 and bl[y][x] == '1':
                c += 1

            if a > 0 and b > 0 and c > 0 and bl[y][x] == '0':
                minalpha = min(a, b, c)
                plus = decode[str(a//minalpha) + str(b//minalpha) + str(c//minalpha)]
                result.append(plus)
                a = b = c = 0
            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
                        (result[1] + result[3] + result[5]) + result[7]
                if value % 10 == 0 and result not in visited:
                    ans += sum(result)
                visited.append(result)
                result = []

    print(f'#{tc} {result}')