# 02/24
# [S/W 문제해결 기본] 6일차 - 계산기3
for tc in range(1, 11):
    N = int(input())
    words = input()
    icp = {'*': 2, '+': 1, '(': 3}  # 입력할 때
    isp = {'*': 2, '+': 1, '(': 0}  # 스택안
    stack = []
    num_list = []
    # 중위표기 -> 후위표기 변경
    for i in range(N):
        if words[i] in '0123456789':
            num_list.append(words[i])
        else:
            if not stack:
                stack.append(words[i])
            else:
                if words[i] == ')':             # 닫는 괄호일 경우
                    while stack[-1] != '(':     # 여는 괄호가 나올때 까지 stack안의 연산자 빼서 num_list에 추가
                        num_list.append(stack.pop())
                    stack.pop()
                elif icp[words[i]] > isp[stack[-1]]:    # stack안의 연산자보다 입력받은 연산자가 더 클 경우
                    stack.append(words[i])              # 그냥 stack에 추가
                else:                                       # stack안의 연산자의 우선순위가 더 높을 경우
                    while icp[words[i]] <= isp[stack[-1]]:  # stack안의 연산자 우선순위가 같거나 작아질때까지 num_list에 추가
                        num_list.append(stack.pop())
                    stack.append(words[i])                  # stack안의 연산자 조건맞게 뺐으면 새로 입력 받은 연산자를 stack에 추가

    # 계산
    cal = []
    for i in range(len(num_list)):
        if num_list[i] in '0123456789':
            cal.append(num_list[i])
        else:
            num2 = int(cal.pop())
            num1 = int(cal.pop())
            if num_list[i] == "+":
                result = num1 + num2
            elif num_list[i] == "*":
                result = num1 * num2
            cal.append(str(result))

    print(f'#{tc} {cal[0]}')