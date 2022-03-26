# 문자열 s에서 반복된 문자를 지우려고 한다.
# 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
# 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
# 다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
# CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
# CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.
# C 1글자가 남았으므로 1을 리턴한다.

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
