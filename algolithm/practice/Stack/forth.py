# 02/24
# 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth
T = int(input())
for tc in range(1, T + 1):
    forth = list(input().split())
    stack = []
    for f in forth:
        if f in '0123456789':           # 숫자일 경우
            stack.append(int(f))        # int로 추가
        else:
            if f == '.':                # 종료조건에서
                if len(stack) == 1:     # 결과 숫자가 1개일 경우
                    result = stack.pop()   # 그냥 출력
                else:                   # 아니면 에러
                    result = 'error'
                break
            if len(stack) >= 2:  # 연산자에 해당하고 계산할 숫자의 개수가 2개 이상일 경우 정상작동
                num2 = stack.pop()  # pop 순서에 따라 연산 순서 주의
                num1 = stack.pop()  # num1이 먼저
                if f == '+':
                    stack.append(num1 + num2)
                elif f == '-':
                    stack.append(num1 - num2)
                elif f == '*':
                    stack.append(num1 * num2)
                elif f == '/':
                    stack.append(num1 // num2)
            else:  # 연산자에 해당하는데 숫자의 개수가 2개가 안될경우
                result = 'error'  # 에러
                break

    print(f'#{tc} {result}')
