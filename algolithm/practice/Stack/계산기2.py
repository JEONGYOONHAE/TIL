# 02/23
# [S/W 문제해결 기본] 6일차 - 계산기2
for tc in range(1, 11):
    who_first = {'*': 2, '+': 1}
    N = int(input())
    number = input()    # str로 받아옴! (int아님 주의)
    stack = []
    num_list = []
    for i in range(N):
        # 1. 숫자일 경우 그냥 numlist에 추가
        if number[i] in '0123456789':
            num_list.append(number[i])
        # 2. 연산자일 경우
        elif number[i] in '*+':
            if not stack:   # 2-1. 스택이 비어있을 경우 그냥 추가
                stack.append(number[i])
            else:   # 2-2. 스택이 비어있지 않고 stack[-1]이 받아오는 연산자보다 우선순위를 가질 경우
                if who_first[stack[-1]] >= who_first[number[i]]:
                    # 2-2-1. stack[-1]이 우선순위가 있을 때까지 반복해서 num_list에 추가하고 stack은 pop을 해준다.
                    while stack and who_first[stack[-1]] >= who_first[number[i]]:
                        num_list.append(stack[-1])
                        stack.pop()
                # 2-2-2. 받아오는 연산자가 우선순위를 가질 경우 그냥 stack에 추가
                stack.append(number[i])
    # 3. 남은 연산자 추가
    while stack:
        num_list.append(stack[-1])
        stack.pop()
    # 4. 계산할 시간
    cal = []
    for n in num_list:
        if n not in '*+':           # 4-1. 숫자일 경우 그냥 추가
            cal.append(int(n))
        elif n == '+':              # 4-2. + 연산자일 경우
            num2 = cal.pop()        # 뒤에 숫자
            num1 = cal.pop()        # 처음 숫자
            cal.append(num1+num2)
        else:                       # 4-3. * 연산자일 경우
            num2 = cal.pop()        # 뒤에 숫자
            num1 = cal.pop()        # 처음 숫자
            cal.append(num1 * num2)

    print(f'#{tc} {int(cal[0])}')

