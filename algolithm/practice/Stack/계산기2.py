# 02/23
# [S/W 문제해결 기본] 6일차 - 계산기2
for tc in range(1, 11):
    N = int(input())
    number = input()
    stack = []
    what_first = {'+':1, '*':2}
    result_arr = []
    # 후위 연산으로 변경
    for n in number:
        top = stack[-1]
        if n in '+*':           # 연산자에 해당할 경우
            if not stack:       # stack이 비어있으면
                stack.append(n) # 그냥 추가
            if what_first[top] < what_first[n]:     # stack이 있고 stack[-1]보다 현재 연산자의 우선순위가 높은 경우
                result_arr.append(n)
            else:   # top의 연산자가 우선순위가 높은 경우
                result_arr.append(top)   # top을 추가 하고
                stack.pop()         # stack안에 top을 pop
                stack.append(n)     # stack에 n 추가
        else:
            result_arr.append(int(n))
    # 계산할 차례,,
    for i in range(result_arr):
        if result_arr[i] in '+*':
            

    print(f'#{tc} {result_arr}')