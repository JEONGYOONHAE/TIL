# 1. 조망권 확보 여부 구하기
# 현재 아파트의 max높이가 앞뒤로 2칸 범위에서 max일 경우 조망권 확보 가능
# 2. 조망권 확보 가구 수를 구하기

T = 10
for tc in range(1, T+1):
    width = int(input())
    height = list(map(int, input().split()))    # 아파트의 높이

    # 앞뒤로 2칸은 조망권 확보할 필요 없음
    for i in range(2, width-2):
        # 현재 기준에서 -2:2 범위의 max높이 구하기
        neighbor = [height[i-2], height[i-1], height[i+1], height[i+2]]
        max_neighbor = max(neighbor)
        # max_neighbor = 0
        # for j in can_see:
        #     if j > max_neighbor:
        #         max_neighbor = j
        myview = 0
        if height[i] > max_neighbor:
            myview += height[i] - max_neighbor  # 조망권 확보되는 가구수 만큼 +=

    print(f'#{tc} {myview}')



