for _ in range(1, 11):
    # test case, 길의 총 개수
    tc, v = map(int, input().split())
    # 간선정보를 리스트로 입력받음
    lst = list(map(int, input().split()))
    # 간선정보를 노드별로 입력할 딕셔너리
    arr = {x:[] for x in range(100)}
    for i in range(0, v*2, 2):
        v = lst[i]
        e = lst[i+1]
        arr[v].append(e)
    stack = [0]     # 0에서 시작하기 때문에 0을 넣고 출발
    visited = [0]*100
    visited[0] = 1  # 0에서 시작하므로 0 방문 경험 있음
    answer = 0      # 결과값
    while stack:
        now = stack.pop()
        for n in arr[now]:
            # 99로 가는 길이 있으면 성공
            if n == 99:
                answer = 1
                break
            # 방문경험이 없으면 stack과 visited에 추가하고 계속 진행
            if not visited[n]:
                stack.append(n)
                visited[n] = 1

    print(f'#{tc} {answer}')





