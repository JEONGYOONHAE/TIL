# 02/23
# [S/W 문제해결 기본] 6일차 - 계산기2 (2) : 다시 작성해봄
for tc in range(1, 11):
    N = int(input())
    number = input()
    what_first = {'*':2, '+':1}
    stack = []
    result = []
    # 1. 받은 중위표기식 문자열을 후위표기로 변환
    for i in range(number):
        if number[i] in '0123456789':       # 숫자일 경우
            result.append(number[i])        # 그냥 추가
        if not stack:
            stack.append(number[i])         # 연산자일 경우
        else:
            if what_first[stack[-1]] > what_first[number[i]]:                   # stack[-1]의 우선순위가 높을 경우
                while stack and what_first[stack[-1]] > what_first[number[i]]:  # stack[-1]보다 number[i]가 높은 경우가 나오기 전까지
                    result.append(stack[-1])                                    # result에 추가
                    stack.pop()                                                 # stack에서는 pop
            else:
                stack.append(number[i])                                         # number[i]의 우산선위가 높은 경우 그냥 추가

    while stack:                    # stack이 남아있으면
        result.append(stack[-1])    # 추가
        stack.pop(-1)

    # 2. 후위표기로 받은 문자열을 연산자에 맞게 계산
    cal = []    # 계산을 받을 리스트
    for i in range(len(result)):
        if result[i] == '+':            # + 연산자일 경우
            num2 = stack.pop()
            num1 = stack.pop()
            cal.append(num1 + num2)
        elif result[i] == '*':          # * 연산자일 경우
            num2 = stack.pop()
            num1 = stack.pop()
            cal.append(num1 * num2)
        else:                           # 숫자일 경우 그냥 추가
            cal.append(int(result[i]))
