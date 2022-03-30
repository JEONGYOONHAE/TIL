# 02/22
# 4873.[파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

# stack을 통해서 새로입력 받은 문자가 stack의 top과 일치하는지 확인하고 지우기 / 진행하기
T = int(input())
for tc in range(1, T+1):
    name = input()
    stack = []
    top = -1
    # for문 이용
    for i in range(len(name)):
        if stack:   # stack이 비어있지 않을 경우
            if stack[top] == name[i]:   # stack[top]과 입력받은 문자를 비교
                stack.pop()             # 일치할 경우 stack에서 삭제
            else:
                # stack[top]과 입력받은 문자가 일치하지 않는 경우
                stack.append(name[i])   # stack 추가
        else:
            stack.append(name[i])

    # while문 이용
    i = 0   # name의 인덱스
    while i < len(name):
        if stack:
            if stack[top] == name[i]:
                stack.pop()
            else:
                stack.append(name[i])
        else:
            stack.append(name[i])
        i += 1
        
    print(f'#{tc} {len(stack)}')
